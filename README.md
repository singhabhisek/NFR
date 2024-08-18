# NFR InsightIQ Website Help Guide

## Overview
The NFR InsightIQ platform provides a comprehensive suite of tools and dashboards for managing and analyzing non-functional requirements (NFRs). This guide will walk you through the functionalities of the various screens within the platform, as well as explain the different controls and their potential meanings.

## Table of Contents
1. [Landing Page – Dashboard](#landing-page--dashboard)
2. [Compare Releases](#compare-releases)
3. [Discrepancy Search in SLA](#discrepancy-search-in-sla)
4. [Upload NFR Screen](#upload-nfr-screen)
5. [File Service Dependency Upload Screen](#file-service-dependency-upload-screen)
6. [User Access Management](#user-access-management)

---

## 1. Landing Page – Dashboard

### Overview
The Landing Page serves as the main dashboard upon logging in. It provides a summary of key metrics and quick links to other parts of the platform.

### Features
- **Key Metrics**: Displays crucial information related to NFRs, such as compliance status and recent updates.
- **Quick Navigation**: Offers easy access to commonly used screens like Compare Releases, Upload NFR Screen, and User Access Management.
- **Search Bar**: Allows users to search for specific data across the platform.

### Mandatory Fields
- **Search Bar**: A keyword is required to perform a search.

### Possible Values
- **Search Keywords**: Terms related to NFRs, release names, or specific SLA identifiers.

### Controls
- **Dashboard Widgets**: Interactive elements showing real-time data on NFRs.
- **Navigation Menu**: Provides easy access to different sections of the platform.

---

## 2. Compare Releases

### Overview
The Compare Releases screen allows users to compare NFR data between different software releases.

### Features
- **Release Selection**: Users can select specific software versions to compare.
- **Comparison Results**: Provides a detailed view of differences in NFRs between the selected releases.
- **Export Option**: Allows users to export comparison results.

### Mandatory Fields
- **Release 1**: Required to select the first software release version.
- **Release 2**: Required to select the second software release version.

### Possible Values
- **Release Versions**: Examples include "v1.0," "v1.1," etc.

### Controls
- **Release Dropdowns**: Select the software versions for comparison.
- **Compare Button**: Initiates the comparison process.
- **Export Button**: Allows downloading the comparison results in various formats (e.g., CSV).

---

## 3. Discrepancy Search in SLA

### Overview
The Discrepancy Search in SLA screen helps users identify discrepancies in Service Level Agreements (SLAs) related to NFRs.

### Features
- **Search Filters**: Allows users to apply various filters to narrow down search results.
- **Discrepancy Results**: Displays identified discrepancies based on selected criteria.
- **Detailed View**: Offers more information on selected discrepancies. Click on any discrepancy to view more details, including the potential impact on the SLA.

### Mandatory Fields
- **NFR Details**: Selecting an NFR detail to compare is mandatory.

### Possible Values
- **NFR Details**: Could include categories like Application, Release or Transactions.

### Controls
- **Search Button**: Executes the search based on the provided filters.
- **Filter Options**: Include date ranges, NFR categories, and severity levels.
- **Details Button**: Opens a detailed view of the selected discrepancy.

---

## 4. Upload NFR Screen

### Overview
The Upload NFR Screen allows users to upload NFR data files into the platform.

### Features
- **File Upload**: Users can drag-and-drop or select files to upload.
- **Validation**: The system automatically checks the uploaded files for format compliance, ensuring that all required fields are present and correctly formatted.
- **Upload History**: Tracks the status and history of previous uploads, allowing users to review and troubleshoot as necessary.

### Mandatory Fields
The following fields must be present and correctly filled out in the uploaded NFR file:
1. **ApplicationName**: Required. The name of the application (e.g., "Mobile").
2. **ReleaseID**: Required. The identifier for the release (e.g., "R2023").
3. **BusinessScenario**: Required. Describes the business scenario being tested.
4. **TransactionName**: Required. The name of the transaction associated with the NFR.
5. **SLA**: Required. The Service Level Agreement time in seconds.
6. **TPS**: Required. Transactions per second, representing the throughput.
7. **Comments**: Optional. Any additional notes or remarks.

### Possible Values
- **ApplicationName**: Must match the exact name recognized by the platform.
- **ReleaseID**: Format "YYYY.MM" (e.g., "R2023").
- **BusinessScenario**: Descriptive name for the business process.
- **TransactionName**: Concise transaction name, ideally structured.
- **SLA**: Numeric values representing time in seconds.
- **TPS**: Numeric values representing transaction throughput.
- **Comments**: Free text for any relevant additional information.

### Controls
- **Upload Button**: Starts the file upload process. The system validates the data and provides feedback on any issues.
- **Validation Results**: Displays errors or warnings found during validation.
- **History Log**: View previous uploads with timestamps, statuses, and issues encountered.

---

## 5. File Service Dependency Upload Screen

### Overview
The File Service Dependency Upload Screen allows users to upload files describing dependencies between different services.

### Features
- **Dependency Mapping**: Helps visualize and manage service dependencies after file upload.
- **Upload Functionality**: Validates the uploaded files to ensure that all required fields are present and formatted correctly.

### Mandatory Fields
The following fields must be present and correctly filled out in the uploaded dependency file:
1. **ApplicationName**: Required. The name of the application (e.g., "Online," "Mobile").
2. **ReleaseID**: Required. The identifier for the release (e.g., "R2021," "R2022").
3. **BusinessScenario**: Required. Describes the business scenario being tested.
4. **TransactionName**: Required. The name of the transaction associated with the dependency.
5. **BackendCall**: Required. The backend service or API name (e.g., "WS_CreditCard").
6. **CallType**: Required. Indicates whether the call is synchronous ("Sync") or asynchronous ("Async").

### Possible Values
- **ApplicationName**: Must be an exact match to a recognized application name.
- **ReleaseID**: Format "YYYY.MM" (e.g., "2021.3").
- **BusinessScenario**: A descriptive title for the business process.
- **TransactionName**: Unique name for the transaction within the scenario.
- **BackendCall**: Name of the backend service or API.
- **CallType**: "Sync" for synchronous calls, "Async" for asynchronous calls.

### Controls
- **Upload Button**: Starts the file upload process. The system validates the dependency data and visualizes it.
- **Dependency Graph**: Displays the service dependencies, aiding in impact analysis.

---

## 6. User Access Management

### Overview
The User Access Management screen allows administrators to manage user permissions within the platform.

### Features
- **User Roles**: Assign and manage roles (e.g., Admin, User, Viewer) to control access levels.
- **Access Control**: Define what each role can view or edit within the platform.
- **Audit Logs**: Keep track of changes made to user permissions for security purposes.

### Mandatory Fields
- **User Name**: Required when creating or modifying user accounts.
- **Role Assignment**: A role must be selected when assigning permissions.

### Possible Values
- **User Roles**: Options include "Admin," "User," and "Viewer."
- **Access Levels**: These may vary depending on the role, such as "Read Only" or "Full Access."

### Controls
- **Add User**: Creates new user accounts.
- **Role Dropdown**: Selects the role to assign to a user.
- **Save Button**: Saves any changes made to user accounts or permissions.

---

This help guide provides detailed instructions on how to use the NFR InsightIQ platform, including mandatory fields, possible values, and controls for each screen. For further questions, please reach out to the TEAM.
