/**
 * Supabase Database Initialization & Migrations
 * Creates SQL tables for user authentication, roles, audit logs, and operational telemetry.
 */
const bcrypt = require('bcryptjs');
const { query, testConnection } = require('./db');

async function initDatabase() {
  console.log('[Database] Testing connection to Supabase PostgreSQL...');
  const health = await testConnection();
  if (!health.connected) {
    console.error('[Database] Failed to connect to Supabase:', health.error);
    return false;
  }
  console.log(`[Database] Successfully connected to Supabase (${health.database}) on ${health.host}`);

  try {
    // 1. Create Users Table
    await query(`
      CREATE TABLE IF NOT EXISTS nwis_users (
        id SERIAL PRIMARY KEY,
        user_uuid UUID DEFAULT gen_random_uuid() UNIQUE,
        email VARCHAR(255) UNIQUE NOT NULL,
        password_hash VARCHAR(255) NOT NULL,
        full_name VARCHAR(255) NOT NULL,
        organization VARCHAR(255) DEFAULT 'DGH / MoPNG',
        role VARCHAR(100) DEFAULT 'Drilling Operations Engineer',
        clearance_level VARCHAR(50) DEFAULT 'Level-3 (Confidential)',
        assigned_basin VARCHAR(100) DEFAULT 'Assam-Arakan & Western Offshore',
        phone VARCHAR(50) DEFAULT '+91 (0) 11 2617 0100',
        is_active BOOLEAN DEFAULT TRUE,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP WITH TIME ZONE
      );
    `);
    console.log('[Database] Table "nwis_users" verified/created.');

    // 2. Create User Audit Log Table
    await query(`
      CREATE TABLE IF NOT EXISTS nwis_audit_logs (
        id SERIAL PRIMARY KEY,
        user_email VARCHAR(255),
        action VARCHAR(100) NOT NULL,
        details JSONB,
        ip_address VARCHAR(100),
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
      );
    `);
    console.log('[Database] Table "nwis_audit_logs" verified/created.');

    // 3. Create Session Tokens Table
    await query(`
      CREATE TABLE IF NOT EXISTS nwis_sessions (
        id SERIAL PRIMARY KEY,
        token_hash VARCHAR(255) UNIQUE NOT NULL,
        user_id INTEGER REFERENCES nwis_users(id) ON DELETE CASCADE,
        expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
      );
    `);
    console.log('[Database] Table "nwis_sessions" verified/created.');

    // 4. Seed default superadmin / engineer if not present
    const existingAdmin = await query('SELECT id FROM nwis_users WHERE email = $1', ['admin@nwis.gov.in']);
    if (existingAdmin.rows.length === 0) {
      const defaultHash = await bcrypt.hash('Admin@123', 10);
      await query(`
        INSERT INTO nwis_users (email, password_hash, full_name, organization, role, clearance_level, assigned_basin)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
      `, [
        'admin@nwis.gov.in',
        defaultHash,
        'Chief Geologist & Drilling Superintendent',
        'Directorate General of Hydrocarbons (DGH)',
        'Superintendent Engineer',
        'Level-1 (Top Secret / MoPNG Directorate)',
        'All Indian Basins (Category-I / II / III)'
      ]);
      console.log('[Database] Seeded default superadmin: admin@nwis.gov.in / Admin@123');
    }

    const existingEngineer = await query('SELECT id FROM nwis_users WHERE email = $1', ['engineer@ongc.co.in']);
    if (existingEngineer.rows.length === 0) {
      const engHash = await bcrypt.hash('Engineer@123', 10);
      await query(`
        INSERT INTO nwis_users (email, password_hash, full_name, organization, role, clearance_level, assigned_basin)
        VALUES ($1, $2, $3, $4, $5, $6, $7)
      `, [
        'engineer@ongc.co.in',
        engHash,
        'Rajesh Sen (Senior Subsurface Engineer)',
        'ONGC Offshore Subsurface Division',
        'Senior Reservoir Analyst',
        'Level-2 (Restricted Operational)',
        'Western Offshore & KG Basin'
      ]);
      console.log('[Database] Seeded default engineer: engineer@ongc.co.in / Engineer@123');
    }

    return true;
  } catch (err) {
    console.error('[Database Migration Error]:', err.message);
    return false;
  }
}

module.exports = {
  initDatabase
};

if (require.main === module) {
  initDatabase().then((success) => {
    console.log('[Database Init Result]:', success ? 'SUCCESS' : 'FAILED');
    process.exit(success ? 0 : 1);
  });
}
