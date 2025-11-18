# 📘 Product Requirements Document (PRD)

## **Project: CampusCompanion**

## **Version: 1.0**

## **Timeline: 24 Nov 2025 → 28 Feb 2026**

# 1. Problem Statement

College campuses face fragmented information and inefficient workflows. Students frequently miss updates, struggle with manual tasks, and lack a unified digital system for everyday campus needs. Key issues include:
* Mess menu shown only on notice boards
* Missed club events and academic deadlines
* No consolidated class timetable
* Manual hostel complaint systems
* No centralized attendance or study material access
* Poor real-time communication between students and administrators

This leads to confusion, missed opportunities, and reduced campus engagement.

# 2. Proposed Solution

**CampusCompanion** will be a unified **mobile + web platform** designed to centralize all essential student services.

### The platform will provide:
* Daily mess menu updates
* Class schedule with alerts
* Hostel complaint system with tracking
* Study resources repository
* Events & club updates
* Lost-and-found board
* Bus/shuttle live tracking (optional)

### Access Points:
* **Student Mobile App**
* **Admin & Faculty Web Dashboard**

# 3. Objectives and Expected Outcomes

### **Objectives**
* Digitize and simplify routine student life operations
* Serve as a one-stop platform for all campus interactions
* Improve student–admin communication and transparency
* Provide real-time updates and actionable information

### **Expected Outcomes**
* 30–40% improvement in communication efficiency
* Reduced manual workload for hostel wardens/admins
* Better student satisfaction and campus engagement
* Push notification–based updates for time-sensitive alerts
* Centralized repository for academic notes and resources

# 4. Tools, Technologies, and Frameworks

### **MERN Stack**

* **Frontend:** React.js (Web), React Native (App)
* **Backend:** Node.js + Express.js
* **Database:** MongoDB Atlas

### Additional Tools

* Figma (UI/UX design)
* Trello / Jira (Task management)
* GitHub (Version control)
* Firebase Cloud Messaging / OneSignal (Push notifications)

# 5. Tentative Milestones & Timeline
**Project Duration: 14 weeks (24 Nov 2025 → 28 Feb 2026)**

| Week | Timeline        | Task/Milestone                            |
| ---- | --------------- | ----------------------------------------- |
| 1    | 24 Nov – 30 Nov | PRD Finalization + UI/UX Wireframes       |
| 2    | 1 Dec – 7 Dec   | Database Schema + Backend Setup           |
| 3    | 8 Dec – 14 Dec  | Authentication + User Roles               |
| 4    | 15 Dec – 21 Dec | Timetable Module + Notification Engine    |
| 5    | 22 Dec – 28 Dec | Mess Menu System + Rating Logic           |
| 6    | 29 Dec – 4 Jan  | Hostel Complaint System (Student + Admin) |
| 7    | 5 Jan – 11 Jan  | Events & Clubs Module                     |
| 8    | 12 Jan – 18 Jan | Study Resources Hub + File Uploads        |
| 9    | 19 Jan – 25 Jan | Lost & Found Module                       |
| 10   | 26 Jan – 1 Feb  | Bus Tracking (Optional)                   |
| 11   | 2 Feb – 8 Feb   | Integration + Debugging                   |
| 12   | 9 Feb – 15 Feb  | System Testing + Bug Fixes                |
| 13   | 16 Feb – 22 Feb | UI Polish + Admin Panel Finalization      |
| 14   | 23 Feb – 28 Feb | Deployment + Final Demo Preparation       |

# 6. Wireframes (Low‑Fidelity)

### **6.1 Student Mobile App – Home Screen**

```
 -----------------------------------
| CampusCompanion                   |
 -----------------------------------
|  [Today's Mess Menu]              |
|   Dal, Rice, Roti, Paneer…       |
 -----------------------------------
|  [Next Class]                     |
|   DS Class - 10:00 AM             |
 -----------------------------------
|  Quick Actions:                   |
|  [Timetable] [Complaints]         |
|  [Events]     [Resources]         |
 -----------------------------------
```

### **6.2 Hostel Complaint Module (Student)**

```
 -----------------------------------
| Raise Complaint                   |
 -----------------------------------
| Category:  Water / Fan / Wifi     |
| Description:  ..................  |
| Photo Upload:  [+]                |
| [Submit Ticket]                   |
 -----------------------------------
```

### **6.3 Admin Dashboard – Complaint Management**

```
 ---------------------------------------------------
| Complaints Dashboard                               |
 ---------------------------------------------------
| Ticket# | Student | Issue  | Status  | Action      |
| 1021    | Ram     | Wifi   | Raised  | [Assign]    |
| 1022    | Rohan   | Fan    | Pending | [Resolve]   |
 ---------------------------------------------------
```

### **6.4 Study Resources Hub**

```
 -----------------------------------
| Study Materials                    |
 -----------------------------------
| Search: [DS Unit 2]               |
 -----------------------------------
| DS Unit 1  - Notes.pdf            |
| DS Unit 2  - Slides.pptx          |
| ML Assignment  - Doc              |
 -----------------------------------
```

# 7. Final Deliverables

* PRD (this document)
* UI/UX screens (Figma)
* API Contract + Database Schema
* Production-ready App + Web Dashboard
* Deployment on cloud (Render / Vercel / Firebase / AWS)
* Final Demo & Presentation: 28 Feb 2026


# 8. Approval & Sign‑off & Team

- **Prepared by:** Alok Gupta (Team Lead)
- **Team Members:** Akanksha Priyadarshinee Rath, Divyanshu Gupta, Rohit Singh
- **Approval Date:** To be finalized by the mentor
