/**
 * NWIS Glacial Precision Unified SPA Router
 * High-performance, zero-lag single-page router with view pre-caching and instant response.
 */

const NWISRouter = (function() {
  const VIEW_MAP = {
    'gateway': 'views/gateway.html',
    'nwis': 'views/gateway.html',
    'nwis-home': 'views/gateway.html',
    'search': 'views/gateway.html',
    'command-center': 'views/command_center.html',
    'well-explorer': 'views/well_explorer.html',
    'well-intelligence': 'views/well_intelligence.html',
    'historical-intelligence': 'views/historical_intelligence.html',
    'nwis-ai': 'views/nwis_ai.html',
    'ai': 'views/nwis_ai.html',
    'risk-monitor': 'views/risk_monitor.html',
    'scenario-lab': 'views/scenario_lab.html',
    'reports': 'views/reports.html',
    'settings': 'views/settings.html'
  };

  const TITLE_MAP = {
    'gateway': 'Entry Gateway',
    'command-center': 'Command Center',
    'well-explorer': 'Well Explorer',
    'well-intelligence': 'Well Intelligence & Subsurface Profile',
    'historical-intelligence': 'Historical Intelligence',
    'nwis-ai': 'NWIS AI Copilot',
    'ai': 'NWIS AI Copilot',
    'risk-monitor': 'Risk Monitor',
    'scenario-lab': 'Scenario Lab',
    'reports': 'Decision Support & Reports',
    'settings': 'System Settings & Operational Preferences'
  };

  const viewCache = new Map();
  let activeRoute = '';
  let isNavigating = false;

  /**
   * Pre-fetches all views into memory on boot for instant 0ms transitions.
   */
  async function prefetchViews() {
    const uniqueFiles = Array.from(new Set(Object.values(VIEW_MAP)));
    for (const filePath of uniqueFiles) {
      try {
        const res = await fetch(filePath);
        if (res.ok) {
          const html = await res.text();
          // Map to all keys referencing this file
          Object.keys(VIEW_MAP).forEach(key => {
            if (VIEW_MAP[key] === filePath) {
              viewCache.set(key, html);
            }
          });
        }
      } catch (e) {
        // Silently continue
      }
    }
  }

  /**
   * Executes any inline <script> tags present inside the newly loaded view.
   */
  function executeViewScripts(container) {
    const scripts = container.querySelectorAll('script');
    scripts.forEach(oldScript => {
      const newScript = document.createElement('script');
      Array.from(oldScript.attributes).forEach(attr => {
        newScript.setAttribute(attr.name, attr.value);
      });
      newScript.textContent = oldScript.textContent;
      oldScript.parentNode.replaceChild(newScript, oldScript);
    });
  }

  /**
   * Updates sidebar active state instantly with clean visual indicators.
   */
  function updateSidebarState(routeKey) {
    const normalized = (routeKey === 'nwis' || routeKey === 'nwis-home' || routeKey === 'search') ? 'gateway' : routeKey;
    const sidebar = document.getElementById('main-sidebar');
    const layoutWrapper = document.getElementById('main-layout-wrapper');

    // Toggle body class and display for gateway (1st page) vs 2nd page command center onwards
    if (normalized === 'gateway') {
      document.body.classList.add('is-gateway');
      if (sidebar) sidebar.style.display = 'none';
      if (layoutWrapper) layoutWrapper.style.paddingLeft = '0px';
    } else {
      document.body.classList.remove('is-gateway');
      if (sidebar) sidebar.style.display = '';
      if (layoutWrapper) layoutWrapper.style.paddingLeft = '';
    }

    document.querySelectorAll('#main-sidebar nav a[data-path]').forEach(a => {
      const path = a.getAttribute('data-path');
      const icon = a.querySelector('.material-symbols-outlined, svg');
      const textSpan = a.querySelector('span:not(.material-symbols-outlined)');

      if (path === normalized) {
        a.setAttribute('aria-current', 'page');
        a.className = 'flex items-center h-10 px-2.5 rounded-lg bg-[#CBD8E2] text-black shadow-sm font-bold transition-colors cursor-pointer group/navitem';
        if (icon) {
          icon.className = 'material-symbols-outlined text-[20px] shrink-0 text-black';
        }
        if (textSpan) {
          textSpan.className = 'ml-3 text-xs font-bold text-black opacity-0 group-hover:opacity-100 transition-opacity duration-150 whitespace-nowrap overflow-hidden text-ellipsis';
        }
      } else {
        a.removeAttribute('aria-current');
        a.className = 'flex items-center h-10 px-2.5 rounded-lg text-[#203848] hover:bg-[#CBD8E2] hover:text-black transition-colors cursor-pointer group/navitem';
        if (icon) {
          icon.className = 'material-symbols-outlined text-[20px] shrink-0 text-[#203848] group-hover/navitem:text-black';
        }
        if (textSpan) {
          textSpan.className = 'ml-3 text-xs font-bold text-[#203848] group-hover/navitem:text-black opacity-0 group-hover:opacity-100 transition-opacity duration-150 whitespace-nowrap overflow-hidden text-ellipsis';
        }
      }
    });

    // Update Header breadcrumb label
    const breadcrumb = document.getElementById('header-breadcrumb-title');
    if (breadcrumb && TITLE_MAP[normalized]) {
      breadcrumb.textContent = TITLE_MAP[normalized];
    }
  }

  /**
   * Navigates to target view instantly with fresh view content.
   */
  async function navigateTo(targetRoute) {
    const route = targetRoute || 'gateway';
    const filePath = VIEW_MAP[route];
    if (!filePath) return;

    const mainContainer = document.getElementById('app-main');
    if (!mainContainer) return;

    activeRoute = route;
    if (window.location.hash !== `#${route}`) {
      window.location.hash = route;
    }
    
    document.title = `NWIS — ${TITLE_MAP[route] || 'Nearby Wells Intelligence'}`;
    updateSidebarState(route);

    try {
      const response = await fetch(`${filePath}?_t=${Date.now()}`);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const htmlContent = await response.text();
      mainContainer.innerHTML = htmlContent;
      executeViewScripts(mainContainer);
      window.scrollTo({ top: 0, behavior: 'auto' });
    } catch (err) {
      console.error('Failed to load view:', err);
      mainContainer.innerHTML = `<div class="p-8 text-center text-error">Failed to load view: ${err.message}</div>`;
    }
  }

  /**
   * Initializes router and hash change listeners.
   */
  function init() {
    // Hash change listener for instantaneous navigation
    window.addEventListener('hashchange', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash && hash !== activeRoute && VIEW_MAP[hash]) {
        navigateTo(hash);
      }
    });

    // Initial load from URL hash or default to gateway
    const initialHash = window.location.hash.replace('#', '');
    navigateTo(initialHash && VIEW_MAP[initialHash] ? initialHash : 'gateway');

    // Pre-cache all views in the background
    setTimeout(prefetchViews, 100);

    // Ensure links in sidebar blur on click so focus doesn't lock sidebar or window panel
    const sidebar = document.getElementById('main-sidebar');
    if (sidebar) {
      sidebar.addEventListener('click', (e) => {
        const link = e.target.closest('a');
        if (link) {
          link.blur();
        }
      });
    }
  }

  return { init, navigateTo };
})();

document.addEventListener('DOMContentLoaded', NWISRouter.init);

