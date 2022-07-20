# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Types of changes:

- `Added` for new features.
- `Changed` for changes in existing functionality.
- `Removed` for now removed features.

## [Unreleased]

### Removed

- Removed encryption module (containing unimplemented skykey functions).

## [2.4.0]

### Added

- Added Skynet Api Key support (`skynet_api_key`).

## [2.3.0]

### Added

- Fixed `get_metadata`.

## [2.2.0]

_This release adds Windows support._

### Added

- Windows is now fully supported

### Changed

- A bug with directory uploads on Windows has been fixed

## [2.1.0]

### Added

- `upload` and `upload_request` API
- Support for chunked uploading

## [2.0.0]

### Changed

- This SDK has been updated to match Browser JS and require a client. You will
  first need to create a client and then make all API calls from this client.
- Connection options can now be passed to the client, in addition to individual
  API calls, to be applied to all API calls.
- The `defaultPortalUrl` string has been renamed to `defaultSkynetPortalUrl` and
  `defaultPortalUrl` is now a function.

## [1.1.0]

### Added

- `metadata` function
- Upload and download `_request` functions
- Common Options object
- API authentication

### Changed

- Some upload bugs were fixed.

## [1.0.2]

## Added

- Possibility to use chunks

## [1.0.1]

### Changed

- Drop UUID

## [1.0.0]

### Added

- Upload and download functionality.
