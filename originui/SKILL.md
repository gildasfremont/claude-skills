---
name: originui
description: >
  Use this skill whenever the user needs to pick, implement, or understand
  a UI component from coss.com/ui (React), base-ui.com (React primitives),
  or originui-ng.com (Angular). Triggers: which component should I use for X,
  how do I implement a dialog/select/button, show me a coss ui component,
  I need a dropdown/toast/accordion, find me the right UI component,
  implement this UI element. ALWAYS use this skill before writing any UI
  component code to prevent wrong API usage and guessed props.
---

# originui / coss.com/ui Component Skill

## Stack decision

**React project** → use **coss.com/ui** (styled components on Base UI).
**Angular project** → use **originui-ng.com** (RadixNG + Tailwind v4).
**Primitive API detail needed** → consult base-ui reference file.

If unsure, ask the user which stack they're on.

---

## How to use this skill

1. **Identify the right component** using the catalog and decision guide below.
2. **Read the local reference file** for that component's API, props, and code examples.
3. Implement using the exact imports and props — never guess.

### Local reference files

| Source | Path pattern |
|--------|-------------|
| coss.com/ui (React) | `references/components/{slug}.md` |
| base-ui.com (primitives) | `references/base-ui/{slug}.md` |
| Hooks | `references/hooks/{hook}.md` |

**Example**: user needs a Select → read `references/components/select.md` → implement from props + examples.

For complex components (combobox, command, drawer, toast, menu) always read the full reference file — they have multiple sub-components and non-obvious APIs.

---

## Quick decision guide

```
Need a form?              → Field + Input/Select/Checkbox + Form
Need a modal?             → Dialog (general) | AlertDialog (destructive confirm)
Need a side panel?        → Sheet (simple slide-in) | Drawer (swipe + snap points)
Need a dropdown menu?     → Menu
Need a searchable select? → Combobox | Autocomplete
Need date input?          → DatePicker (simple) | Calendar (full control)
Need notification?        → Toast (auto-dismiss) | Alert (persistent callout)
Need loading?             → Spinner (inline) | Skeleton (content placeholder)
Need a settings toggle?   → Switch
Need exclusive options?   → RadioGroup
Need multi-select?        → CheckboxGroup | Combobox (multiple)
Need a command palette?   → Command (Dialog + Autocomplete)
Need keyboard shortcut?   → Kbd
```

---

## Component catalog

### Form inputs

| Component | File | Notes |
|-----------|------|-------|
| Button | `button.md` | variants: default/outline/ghost/destructive/destructive-outline/link/secondary; sizes: xs/sm/default/lg/xl + icon variants; `loading` prop built-in; `render` prop for Link |
| Input | `input.md` | Native input wrapper |
| Textarea | `textarea.md` | Multi-line text |
| Checkbox | `checkbox.md` | Single binary toggle |
| Checkbox Group | `checkbox-group.md` | Multiple checkboxes with shared state |
| Radio Group | `radio-group.md` | Mutually exclusive options |
| Switch | `switch.md` | On/off toggle |
| Slider | `slider.md` | Range value |
| Number Field | `number-field.md` | Numeric with increment/decrement + scrub |
| Select | `select.md` | Predefined dropdown |
| Autocomplete | `autocomplete.md` | Input with filtered suggestions |
| Combobox | `combobox.md` | Input + list, supports single/multiple |
| Input Group | `input-group.md` | Input + addons/buttons grouped |
| Input OTP | `input-otp.md` | Segmented OTP / verification code |
| Field | `field.md` | Label + input + validation wrapper |
| Fieldset | `fieldset.md` | Group of related fields |
| Form | `form.md` | Validation + submission handler |

### Date & time

| Component | File | Notes |
|-----------|------|-------|
| Calendar | `calendar.md` | Single / range / multi-select |
| Date Picker | `date-picker.md` | Calendar inside a Popover |

### Overlays & popups

| Component | File | Notes |
|-----------|------|-------|
| Dialog | `dialog.md` | Modal overlay |
| Alert Dialog | `alert-dialog.md` | Destructive confirmation modal |
| Popover | `popover.md` | Floating container anchored to trigger |
| Tooltip | `tooltip.md` | Hint on hover/focus |
| Preview Card | `preview-card.md` | Rich hover preview for links |
| Sheet | `sheet.md` | Slide-in panel (side=top/right/bottom/left) |
| Drawer | `drawer.md` | Swipe + snap points panel |
| Toast | `toast.md` | Auto-dismiss notification |
| Menu | `menu.md` | Dropdown action list, keyboard nav |
| Command | `command.md` | Command palette = Dialog + Autocomplete |

### Navigation & structure

| Component | File | Notes |
|-----------|------|-------|
| Tabs | `tabs.md` | Switch between panels |
| Accordion | `accordion.md` | Collapsible panels (single/multiple) |
| Collapsible | `collapsible.md` | Single collapsible section |
| Breadcrumb | `breadcrumb.md` | Hierarchical nav |
| Pagination | `pagination.md` | Page navigation |
| Toolbar | `toolbar.md` | Grouped controls |
| Sidebar | `sidebar.md` | Not in references yet — fetch from https://coss.com/ui/docs/components/sidebar.md |

### Display & feedback

| Component | File | Notes |
|-----------|------|-------|
| Avatar | `avatar.md` | Image + fallback |
| Badge | `badge.md` | Status label — variants: default/secondary/outline/destructive/success/warning/info |
| Alert | `alert.md` | Persistent callout (non-modal) |
| Card | `card.md` | Content container |
| Frame | `frame.md` | Framed container |
| Empty | `empty.md` | Empty state |
| Skeleton | `skeleton.md` | Loading placeholder |
| Spinner | `spinner.md` | Loading indicator |
| Progress | `progress.md` | Task completion bar |
| Meter | `meter.md` | Numeric value in known range |
| Table | `table.md` | Tabular data |
| Separator | `separator.md` | Visual divider |
| Kbd | `kbd.md` | Keyboard key display |
| Scroll Area | `scroll-area.md` | Custom scrollbars |

### Controls

| Component | File | Notes |
|-----------|------|-------|
| Toggle | `toggle.md` | Two-state button |
| Toggle Group | `toggle-group.md` | Group of toggles (single/multiple) |
| Group | `group.md` | Visual grouping of controls |
| Label | `label.md` | Accessible label |

---

## originui-ng (Angular) catalog

Install:
```bash
npm install @origin-ui/components @radix-ng/primitives @angular/cdk
```
Import in `style.css`:
```css
@import '@angular/cdk/overlay-prebuilt.css';
@import '@angular/cdk/a11y-prebuilt.css';
```

| Component | Variants | Notes |
|-----------|---------|-------|
| Accordion | 11 | |
| Alert | 6 | |
| Avatar | 9 | |
| Badge | 8 | |
| Breadcrumb | 7 | |
| Button | 14 | |
| Calendar | 1 | |
| Checkbox | 5 | |
| Cropper | 4 | Image crop + avatar uploader |
| Dialog | 2 | |
| Dropdown | 2 | |
| File Upload | 6 | drag & drop, progress, image |
| Input | 11 | |
| Notification | 4 | |
| Pagination | 6 | |
| Popover | 4 | |
| Radio | 9 | |
| Select | 8 | |
| Slider | 11 | |
| Stepper | 7 | |
| Switch | 14 | |
| Table | 8 | |
| Tabs | 8 | |
| Textarea | 4 | |
| Tooltip | 4 | |

For Angular variants: browse `https://www.originui-ng.com/{slug}`.

---

## Setup (React / coss.com/ui)

```bash
pnpm dlx shadcn@latest add @coss/{slug}   # single component
pnpm dlx shadcn@latest add @coss/ui       # all at once
```

CSS variables are shadcn-compatible. Extra tokens: `--destructive-foreground`, `--info`, `--info-foreground`, `--success`, `--success-foreground`.

**`render` prop** — renders as a different element while keeping behavior:
```tsx
<Button render={<Link href="/login" />}>Login</Button>
```

---

## Hooks

| Hook | File |
|------|------|
| useMediaQuery | `references/hooks/use-media-query.md` |
| useCopyToClipboard | `references/hooks/use-copy-to-clipboard.md` |
