/**
 * Supabase PostgreSQL Connection Pool
 */
require('dotenv').config();
const { Pool } = require('pg');

const connectionString = process.env.DATABASE_URL || 
  `postgresql://${process.env.PGUSER}:${process.env.PGPASSWORD}@${process.env.PGHOST}:${process.env.PGPORT}/${process.env.PGDATABASE}`;

const pool = new Pool({
  connectionString,
  ssl: {
    rejectUnauthorized: false
  },
  max: 10,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 10000,
});

pool.on('error', (err) => {
  console.error('[Supabase DB Pool Error]:', err.message);
});

async function query(text, params) {
  const start = Date.now();
  try {
    const res = await pool.query(text, params);
    const duration = Date.now() - start;
    return res;
  } catch (error) {
    console.error('[Supabase SQL Query Error]:', { text, error: error.message });
    throw error;
  }
}

async function testConnection() {
  try {
    const res = await query('SELECT NOW() as db_time, current_database() as db_name, version() as version');
    return {
      connected: true,
      time: res.rows[0].db_time,
      database: res.rows[0].db_name,
      version: res.rows[0].version,
      host: process.env.PGHOST
    };
  } catch (error) {
    return {
      connected: false,
      error: error.message,
      host: process.env.PGHOST
    };
  }
}

module.exports = {
  pool,
  query,
  testConnection
};
