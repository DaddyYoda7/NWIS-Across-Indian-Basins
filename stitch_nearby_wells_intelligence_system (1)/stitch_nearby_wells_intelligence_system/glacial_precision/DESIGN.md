---
name: Glacial Precision
colors:
  surface: '#f5faff'
  surface-dim: '#cfdce6'
  surface-bright: '#f5faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e9f5ff'
  surface-container: '#e3f0fa'
  surface-container-high: '#ddeaf4'
  surface-container-highest: '#d7e4ee'
  on-surface: '#111d24'
  on-surface-variant: '#43474c'
  inverse-surface: '#26323a'
  inverse-on-surface: '#e5f3fd'
  outline: '#73787c'
  outline-variant: '#c3c7cc'
  surface-tint: '#4a6173'
  primary: '#082332'
  on-primary: '#ffffff'
  primary-container: '#203848'
  on-primary-container: '#89a1b4'
  inverse-primary: '#b1cade'
  secondary: '#4a6170'
  on-secondary: '#ffffff'
  secondary-container: '#cae3f5'
  on-secondary-container: '#4e6675'
  tertiary: '#11232c'
  on-tertiary: '#ffffff'
  tertiary-container: '#273842'
  on-tertiary-container: '#8fa1ad'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cde6fa'
  primary-fixed-dim: '#b1cade'
  on-primary-fixed: '#031e2d'
  on-primary-fixed-variant: '#32495a'
  secondary-fixed: '#cde6f8'
  secondary-fixed-dim: '#b1cadb'
  on-secondary-fixed: '#031e2b'
  on-secondary-fixed-variant: '#324a58'
  tertiary-fixed: '#d3e5f2'
  tertiary-fixed-dim: '#b7c9d6'
  on-tertiary-fixed: '#0c1e27'
  on-tertiary-fixed-variant: '#384953'
  background: '#f5faff'
  on-background: '#111d24'
  surface-variant: '#d7e4ee'
typography:
  display:
    fontFamily: IBM Plex Sans
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.02em
  display-mobile:
    fontFamily: IBM Plex Sans
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: IBM Plex Sans
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.015em
  headline-lg-mobile:
    fontFamily: IBM Plex Sans
    fontSize: 22px
    fontWeight: '600'
    lineHeight: 30px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: IBM Plex Sans
    fontSize: 20px
    fontWeight: '500'
    lineHeight: 28px
  headline-sm:
    fontFamily: IBM Plex Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: IBM Plex Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 22px
  body-md:
    fontFamily: IBM Plex Sans
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  body-sm:
    fontFamily: IBM Plex Sans
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-lg:
    fontFamily: IBM Plex Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-md:
    fontFamily: IBM Plex Sans
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: IBM Plex Sans
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-sm: 0.5rem
  gutter-lg: 1.5rem
  margin: 1.5rem
  margin-mobile: 0.75rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1.25rem
  space-xl: 2rem
---

## Brand & Style

This design system is engineered for mission-critical technical software, subsea telemetry, and computational energy exploration. It balances the stark, alpine atmospheric calm of crisp glacial peaks with the high-reliability demands of operational engineering consoles. 

The aesthetic is built on **Technical Frosted Glassmorphism**: ultra-clear translucent planes, razor-thin structural hairpins, and cold alpine atmospheric backdrops. Instead of heavy opacities or playful neon gradients, it leverages icy light diffusion to preserve layered situational awareness without sacrificing data contrast or density. The interface inspires cold clarity, analytical precision, and absolute trust under complex operational monitoring conditions.

## Colors

The palette is derived directly from arctic alpine exposures and deep maritime bedrock:

- **Primary (`#203848` - Astral Nomad):** Deep ocean slate. Delivers maximum contrast for primary typography, vital telemetry data readouts, active status indicators, and prominent interactive controls.
- **Secondary (`#546C7B` - Turbulent Sea):** Mid-tone glacial slate. Used for structural dividers, secondary navigation bars, auxiliary text, and supporting iconography.
- **Tertiary (`#95A7B3` - Meditative):** Mist-toned permafrost grey. Drives inactive states, hairline borders across frosted panels, and subtle telemetry axis marks.
- **Neutral Surface Tone (`#CBD8E2` - Blue Reflection):** Cold reflection wash. Used for secondary pane backdrops, subtle hovered tile accents, and translucent layer tints.
- **Canvas Base (`#E3EDF5` - Diamond White):** The ambient light foundation. Acts as the crystalline sky background against which frosted glass planes float.

### Functional Tint Rules
- **Frosted Container Surface:** `rgba(227, 237, 245, 0.72)` over background telemetry canvas, combined with `backdrop-filter: blur(16px) saturate(140%)`.
- **Frosted Border Stroke:** `rgba(149, 167, 179, 0.35)` with an inner highlight stroke of `rgba(255, 255, 255, 0.65)` along top-left edges.

## Typography

IBM Plex Sans provides the rigorous, engineering-grade clarity required for dense telemetry, spatial maps, and computational analytics. 

- **Display & Large Headlines:** Reserved for primary module overview totals, geographic sector coordinates, and global dashboard headers.
- **Labels:** Rendered with elevated letter spacing and medium-to-bold weights for technical uppercase tagging (e.g., `RGB`, `CMYK`, `FLOW RATE`, `PSI`).
- **Body & Data Grid:** Tuned for high information density with compact line heights that prevent visual fatigue during extended shifts. Numerical figures must use tabular lining figures (`font-variant-numeric: tabular-nums`) across all analytical tables.

## Layout & Spacing

The layout is built around a dense 12-column engineering grid optimized for multi-pane dashboards, telemetry plots, and real-time drill-string readouts.

- **Desktop (1200px+):** 12-column fluid grid, `1.5rem` outer margins, `1rem` gutters. Multi-panel side drawers dock seamlessly into frosted tool rails.
- **Tablet (768px - 1199px):** 8-column layout, `1rem` margins, `0.75rem` gutters. Secondary inspector panes collapse into stacked tabs.
- **Mobile (< 768px):** 4-column compact layout with `0.75rem` outer margins and `0.5rem` gutters. Glass cards stretch full-width to prevent truncation of scientific units.

Component padding adheres strictly to the modular 4px base rhythm (`space-xs` through `space-xl`), sustaining a compact cadence suitable for information-heavy technical screens.

## Elevation & Depth

Visual hierarchy does not rely on dark, heavy drop shadows. Depth is articulated through **optical atmospheric layering and crystalline refraction**:

1. **Canvas (Base Level):** Solid `Diamond White` (`#E3EDF5`) with optional low-contrast topographical vector contours.
2. **Layer 1 - Frosted Worksurfaces (Card Panels, Data Grids):**
   - Background: `rgba(227, 237, 245, 0.65)`
   - Backdrop Blur: `14px`
   - Border: `1px solid rgba(149, 167, 179, 0.45)`
   - Shadow: `0 4px 20px -2px rgba(32, 56, 72, 0.06)`
3. **Layer 2 - Active & Floating Elements (Modals, Context Menus, Tooltips):**
   - Background: `rgba(255, 255, 255, 0.85)`
   - Backdrop Blur: `24px`
   - Top highlight inset: `inset 0 1px 0 0 rgba(255, 255, 255, 0.8)`
   - Border: `1px solid rgba(84, 108, 123, 0.35)`
   - Shadow: `0 12px 32px -4px rgba(32, 56, 72, 0.12), 0 2px 6px 0 rgba(32, 56, 72, 0.04)`

## Shapes

The design system maintains a **Soft (`1`)** shape language, utilizing `0.25rem` (4px) radii for operational buttons, inputs, and tab triggers, moving up to `0.5rem` (8px) for primary analytical cards and module containers. 

This restrained curvature reflects technical precision and structural discipline—avoiding both the harsh edge of brutalist sharp corners and the consumer feel of deep pills. Critical status chips and categorical pills utilize small compact fillets to maintain distinct visual contrast from functional cards.

## Components

### Buttons
- **Primary:** Filled `#203848` (Astral Nomad) background with `#E3EDF5` text. On hover, shifts to `#546C7B` with a subtle `box-shadow: 0 2px 8px rgba(32, 56, 72, 0.2)`. Padding: `0.5rem 1rem`.
- **Secondary (Frosted Glass):** Background `rgba(203, 216, 226, 0.45)`, border `1px solid #95A7B3`, text `#203848`. Hover shifts background to `rgba(203, 216, 226, 0.75)`.
- **Ghost:** Text `#546C7B`, border transparent. On hover: `rgba(203, 216, 226, 0.3)`.

### Cards & Module Containers
- Engineered with frosted glassmorphism: `background: rgba(227, 237, 245, 0.65)`, `backdrop-filter: blur(14px)`, `border: 1px solid rgba(149, 167, 179, 0.45)`, border-radius `0.5rem`.
- Card headers feature an upper metadata strip with `label-sm` technical tags (e.g., sensor serial, coordinate references) separated by a `1px solid rgba(149, 167, 179, 0.25)` divider.

### Input Fields & Selectors
- Background: `rgba(255, 255, 255, 0.7)`. Border: `1px solid #95A7B3`. Border-radius: `0.25rem`.
- Text: `#203848` with placeholder in `#546C7B`.
- Focus State: Border color switches to `#203848` with a subtle outline ring `0 0 0 2px rgba(32, 56, 72, 0.15)`.

### Chips & Badges
- Compact telemetry badges styled with `label-sm` uppercase type.
- Neutral Chip: Background `rgba(203, 216, 226, 0.6)`, text `#203848`, border `1px solid rgba(149, 167, 179, 0.5)`.
- Active Sensor Chip: Inset `#203848` background with `#E3EDF5` text.

### Checkboxes & Radios
- Size: `16px x 16px`. Border: `1.5px solid #546C7B`, background `rgba(255, 255, 255, 0.8)`.
- Checked State: `#203848` fill with a crisp white tick or center dot.

### Telemetry Tables & Data Strips
- Row height: `32px` for high-density tabular tracking.
- Alternating rows tinted with `rgba(203, 216, 226, 0.2)`.
- Cell borders: hairline `1px solid rgba(149, 167, 179, 0.25)`.
- Hover state on rows: `rgba(203, 216, 226, 0.45)`.