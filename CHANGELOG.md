# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Todo]
- Research implementing login system with NUSNET id.

## [Unreleased]

---

## [0.5.1] - 2020-06-28
### Added
- WIP: Adding more complex logic for database queries

## [0.5.0] - 2020-06-12
### Added
- Basic add, get, delete features for new database schema

## [0.4.0] - 2020-06-02
### Added
- Created the AppCard wrapper component for ease of use.
- Implement basic App Cards for other pages like Settings, Help, etc.
- Added transitions for App Cards when switching pages.

### Fixed
- Fixed unique key for each AppCard warning.
- Fixed link and ripple color for navigation bar after react-router implementation.
- Fixed state updating for AnncTable component while unmounted.

## [0.3.0] - 2020-06-01
### Added
- Integrated [react-router](https://reacttraining.com/react-router/).

### Changed
- Rewrote navigation bar to use react-router.

## [0.2.1] - 2020-05-31
### Changed
- Finally standardised global theme using MaterialUI's ThemeProvider.
- Everything looks nicer!

### Fixed
- Delete announcement now deletes based on announcement ID instead of positional index.

## [0.2.0] - 2020-05-30
### Added
- Created **App Cards**, a container for content from different pages.
- Added 'New Announcement' and 'Past Announcements' app cards to the home page.

## [0.1.1] - 2020-05-28
### Added
- Added favicon

### Changed
- Link colors now match the theme
- Tidied code for consistency

## [0.1.0] - 2020-05-27
### Added
- React website layout (top bar, navigation menu, content space)
- Started using [MaterialUI framework](https://material-ui.com/) for React
- Express API server for database connection