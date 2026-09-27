/**
 * NWIS Glacial Precision Universal Navigation Bridge
 * Enables seamless cross-page routing and framework messaging
 * without altering any DOM element or visual design token.
 */
(function() {
  const ROUTE_MAP = {
    'nwis': '../nwis_entry_gateway_glacial_light_edition/code.html',
    'nwis-home': '../nwis_entry_gateway_glacial_light_edition/code.html',
    'gateway': '../nwis_entry_gateway_glacial_light_edition/code.html',
    'search': '../nwis_entry_gateway_glacial_light_edition/code.html',
    'command-center': '../nwis_command_center_glacial_minimal_edition_page_02/code.html',
    'well-explorer': '../nwis_well_explorer_glacial_minimal_edition_page_03/code.html',
    'well-intelligence': '../nwis_well_intelligence_w_204_profile_page_04/code.html',
    'historical-intelligence': '../nwis_historical_intelligence_institutional_memory_page_05/code.html',
    'risk-monitor': '../nwis_risk_monitor_proactive_subsurface_intelligence_page_06/code.html',
    'ai-copilot': '../nwis_well_intelligence_w_204_profile_page_04/code.html',
    'scenario-lab': '../nwis_scenario_lab_interactive_decision_support_page_08/code.html',
    'reports': '../nwis_reports_decision_support_minimalist_editorial_dossier/code.html',
    'settings': '../nwis_entry_gateway_glacial_light_edition/code.html'
  };

  document.addEventListener('click', function(e) {
    // 1. Check for data-path links
    const link = e.target.closest('a[data-path], a[title], button#btn-view-well');
    if (!link) return;

    let targetPath = link.getAttribute('data-path');
    
    // Fallback for special buttons
    if (!targetPath && link.id === 'btn-view-well') {
      targetPath = 'well-intelligence';
    }

    // Fallback matching on title or link text
    if (!targetPath && link.getAttribute('title')) {
      const title = link.getAttribute('title').toLowerCase();
      if (title.includes('command center')) targetPath = 'command-center';
      else if (title.includes('well explorer')) targetPath = 'well-explorer';
      else if (title.includes('well intelligence')) targetPath = 'well-intelligence';
      else if (title.includes('historical')) targetPath = 'historical-intelligence';
      else if (title.includes('risk monitor')) targetPath = 'risk-monitor';
      else if (title.includes('scenario lab')) targetPath = 'scenario-lab';
      else if (title.includes('report') || title.includes('decision support')) targetPath = 'reports';
      else if (title.includes('nwis') || title.includes('search')) targetPath = 'nwis';
    }

    if (targetPath && ROUTE_MAP[targetPath]) {
      e.preventDefault();
      // If embedded in parent framework
      if (window.parent && window.parent !== window) {
        window.parent.postMessage({ type: 'NWIS_NAVIGATE', path: targetPath }, '*');
      } else {
        window.location.href = ROUTE_MAP[targetPath];
      }
    }
  });

  // Global search shortcut (Ctrl+K)
  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      const searchInput = document.querySelector('input[type="text"], input[type="search"]');
      if (searchInput) searchInput.focus();
    }
  });
})();
