# Rozoom — Sprint Plan and Review Log

**Module:** SOFT060 — Software Development and Data Science Project  
**University:** University of Plymouth  
**Academic Year:** 2025/2026  
**Methodology:** Agile (Scrum-inspired, five two-week sprints)

---

## Sprint Overview

| Sprint | Focus | Dates | Status |
|--------|-------|-------|--------|
| Sprint 0 | Project initiation and environment setup | 2 Mar – 15 Mar 2026 | Complete |
| Sprint 1 | Core GUI structure and main menu | 16 Mar – 29 Mar 2026 | Complete |
| Sprint 2 | JSON integration and category selection | 30 Mar – 12 Apr 2026 | Complete |
| Sprint 3 | Quiz functionality | 13 Apr – 26 Apr 2026 | Complete |
| Sprint 4 | Manage flashcards, final testing and polish | 27 Apr – 29 Apr 2026 | Complete |

---

## Sprint 0 — Project Initiation and Environment Setup

**Sprint dates:** 2 March 2026 – 15 March 2026  
**Sprint goal:** Establish the project scope, set up the development environment, and define the initial product backlog.

### Sprint Rationale

Sprint 0 is a foundational sprint with no deliverable code. Its purpose is to ensure the developer is fully prepared before any implementation begins. Without a clearly defined scope, development environment, and risk register in place, subsequent sprints would lack direction and structure.

### Sprint Backlog

| Backlog Item | Description | Priority | Status |
|-------------|-------------|----------|--------|
| Define project idea and scope | Decide on Rozoom as a Python desktop flashcard application; confirm suitability with module brief requirements | Must | Complete |
| Research similar applications | Review Quizlet and comparable tools to identify gaps and inform design decisions | Must | Complete |
| Set up development environment | Install Python 3, tkinter, PyCharm IDE; confirm all tools are working correctly on development machine | Must | Complete |
| Configure version control | Create GitHub repository; establish commit workflow for ongoing version tracking throughout the project | Must | Complete |
| Create initial product backlog | List all planned features using MoSCoW prioritisation (Must, Should, Could, Won't) | Must | Complete |
| Conduct risk analysis | Identify risks including hardware failure, skill gaps, scope creep, and health-related time loss; define mitigation strategies | Must | Complete |
| Draft and submit project plan | Write background, aims and objectives, and sprint schedule | Must | Complete |

### Sprint Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Hardware failure / data loss | High | High | GitHub version control and OneDrive backup in place from Sprint 0 |
| Health-related time loss | Medium | High | MoSCoW prioritisation ensures critical features are built first; scope can be reduced if needed |
| Scope too large | Medium | High | Web version descoped in Sprint 0; desktop-only approach confirmed as appropriate |
| Skill gaps in tkinter | Low | Medium | Python Standard Library documentation reviewed; tkinter tutorials consulted prior to Sprint 1 |

### Sprint Review Report

#### Completed Items

| Item | Status | Notes |
|------|--------|-------|
| Project scope defined — Rozoom desktop flashcard application | Complete | Confirmed suitable for module requirements |
| Development environment configured — Python 3, PyCharm, tkinter | Complete | All tools installed and tested on development machine |
| GitHub repository created and configured | Complete | Version control operational from this sprint onwards |
| Initial product backlog created with MoSCoW priorities | Complete | Backlog shared with module supervisor during scrum meeting |
| Risk register completed with mitigation plans | Complete | Four key risks identified; all have documented mitigation strategies |
| Final project plan submitted by 12 March 2026 deadline | Complete | Submitted via DLE on time |

#### Incomplete / Carry-Forward Items

No items were left incomplete in Sprint 0. All initiation activities were completed prior to the 12 March 2026 submission deadline.

#### Items to Address in Next Sprint

Begin implementation of the core tkinter window and main menu structure. Create placeholder functions for all planned buttons. Define all global variables required across the application.

#### Stakeholder Feedback and Product Backlog Adaptations

Module supervisor reviewed the project scope during a scrum meeting and confirmed that a Python desktop flashcard application was appropriate in terms of complexity and scope for the module requirements. No changes to the backlog were required following this meeting.

---

## Sprint 1 — Core GUI Structure and Main Menu

**Sprint dates:** 16 March 2026 – 29 March 2026  
**Sprint goal:** Build the foundational graphical user interface using tkinter, including the main application window, all menu buttons, global state variables, and the screen-switching logic that will underpin the rest of the application.  
**Key milestone:** 29 March 2026 — Working main menu window with all primary navigation buttons.

### Sprint Rationale

Establishing the GUI skeleton in Sprint 1 is critical because all subsequent sprints build upon this structure. Without a working window, navigation system, and global state, the quiz logic, JSON integration, and flashcard management features developed in later sprints have no foundation to attach to.

### Sprint Backlog

| Backlog Item | Description | Priority | Status |
|-------------|-------------|----------|--------|
| Create main tkinter window | Set up the Rozoom window with title, dimensions (400×520px), and basic layout using pack geometry manager | Must | Complete |
| Add status label | Create a status bar below the title that will display all user feedback messages throughout the application | Must | Complete |
| Define global variables | Declare selected_category, current_answer, score, question_index, filtered_questions, and FLASHCARDS_FILE at module level | Must | Complete |
| Create main menu buttons | Implement Start Quiz, Choose Category, Add Flashcard, and Manage Flashcards buttons with correct command bindings | Must | Complete |
| Create quiz UI widgets | Define quiz_question_label, quiz_answer_entry, check_button, next_button, and back_button — hidden by default | Must | Complete |
| Implement screen-switching logic | Build go_back() function using pack() and pack_forget() to swap between menu and quiz views | Must | Complete |
| Stub placeholder functions | Create empty function definitions for all planned features so the app runs without errors | Should | Complete |

### Sprint Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| tkinter layout bugs | Low | Medium | Resolved by using pack() geometry manager consistently throughout; grid() layout avoided |
| Global variable conflicts | Low | High | All shared state declared at module level with explicit 'global' keyword in each function |

### Sprint Review Report

#### Completed Items

| Item | Status | Notes |
|------|--------|-------|
| Main tkinter window created — 400×520px, titled 'Rozoom' | Complete | Window launches and displays correctly on development machine |
| Status label present below title heading | Complete | Updates correctly when tested with hardcoded messages |
| All six global variables declared at module level | Complete | selected_category, score, question_index, current_answer, filtered_questions, FLASHCARDS_FILE |
| Four menu buttons created and visible on launch | Complete | Start Quiz, Choose Category, Add Flashcard, Manage Flashcards all present |
| Quiz UI widgets created and hidden by default | Complete | pack_forget() confirmed working — widgets invisible until quiz starts |
| go_back() function implemented and tested | Complete | Returns user cleanly to main menu from quiz screen |

#### Incomplete / Carry-Forward Items

No items were left incomplete in Sprint 1. The full application skeleton was in place by the end of the sprint, ready for feature implementation in Sprint 2.

#### Items to Address in Next Sprint

Implement the JSON data layer — load_flashcards() and save_flashcards() functions. Build choose_category() to extract unique categories from the data file and display them in a popup window.

#### Stakeholder Feedback and Product Backlog Adaptations

Informal review of the running window confirmed the layout was clean and readable. The four-button main menu structure was considered appropriate for the intended user group.

---

## Sprint 2 — JSON Integration and Category Selection

**Sprint dates:** 30 March 2026 – 12 April 2026  
**Sprint goal:** Connect the application to its persistent data source by implementing the JSON file reading and writing functions, and build the category selection feature that allows users to filter flashcards by topic before starting a quiz.  
**Key milestone:** 12 April 2026 — Application successfully reads from and writes to flashcards.json.

### Sprint Rationale

Data integration is the most critical dependency in the application. Without a working connection to flashcards.json, none of the quiz, add, edit, or delete features can function. This sprint resolves the core data layer and unblocks all remaining feature development.

### Sprint Backlog

| Backlog Item | Description | Priority | Status |
|-------------|-------------|----------|--------|
| Create flashcards.json | Design and populate the JSON data structure with category, question, and answer fields; add sample AI and Cyber Security flashcards | Must | Complete |
| Implement load_flashcards() | Read and parse the JSON file; handle missing file (os.path.exists) and corrupted file (try/except) gracefully | Must | Complete |
| Implement save_flashcards() | Write the full flashcard list back to the JSON file using json.dump() with indent=4 formatting | Must | Complete |
| Fix broken import statement | Remove incorrect 'import flashcards' line; add correct 'import json' and 'import os' statements | Must | Complete |
| Implement choose_category() | Extract unique categories from loaded data using a for-loop; display as buttons in a Toplevel popup with grab_set() | Must | Complete |
| Add category confirmation to status bar | Update status_label with selected category name after user makes a selection | Should | Complete |
| Add empty data error handling | Display a clear message in the status bar if no flashcards are found in the file | Should | Complete |

### Sprint Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| JSON file missing at runtime | Low | High | os.path.exists() check added before any file open attempt; returns empty list safely |
| Corrupted JSON file | Low | Medium | try/except block catches JSONDecodeError and IOError; returns empty list without crashing |

### Sprint Review Report

#### Completed Items

| Item | Status | Notes |
|------|--------|-------|
| flashcards.json created with AI and Cyber Security categories | Complete | 6 sample cards across 2 categories; correct JSON array structure confirmed |
| load_flashcards() reads data and returns Python list | Complete | Tested with valid file, missing file, and corrupted file — all handled correctly |
| save_flashcards() writes updated list to file | Complete | File written with indent=4; human-readable output confirmed |
| Import error resolved — 'import json' and 'import os' added | Complete | Root cause of original data connection bug eliminated |
| choose_category() popup displays category buttons | Complete | Popup uses Toplevel with grab_set(); closes cleanly after selection |
| Status bar confirms category selection | Complete | Shows 'Category: Cybersecurity' style message after user clicks |
| Error message shown when file is empty or missing | Complete | Status bar shows 'No flashcards found! Add some first.' |

#### Incomplete / Carry-Forward Items

All planned items were completed in Sprint 2. The resolution of the import error was the most significant fix, as it unblocked the entire data layer and allowed all subsequent features to be built.

#### Items to Address in Next Sprint

Implement the full quiz flow: start_quiz() to filter and shuffle cards, show_question() to display each card, check_answer() to validate user input, and next_question() to advance through the deck.

#### Stakeholder Feedback and Product Backlog Adaptations

Manual testing confirmed that selecting the 'AI' and 'Cyber Security' categories loaded the correct flashcards into the filtered list. The popup window was confirmed to hold focus correctly using grab_set().

---

## Sprint 3 — Quiz Flow, Answer Checking, and Score Tracking

**Sprint dates:** 13 April 2026 – 23 April 2026  
**Sprint goal:** Implement the complete quiz experience: filtering flashcards by category, shuffling questions randomly, displaying each question with a progress counter, validating user answers case-insensitively, tracking the score, and displaying the final result at the end of the quiz.  
**Key milestone:** 23 April 2026 — Portfolio and code submission deadline.

### Sprint Rationale

The quiz flow is the core functionality of Rozoom and the primary reason the application exists. All prior sprints have been building towards this sprint. Completing a fully functional quiz loop by the submission deadline is the most critical deliverable of the entire project.

### Sprint Backlog

| Backlog Item | Description | Priority | Status |
|-------------|-------------|----------|--------|
| Implement start_quiz() | Filter cards by selected category (case-insensitive); call random.shuffle(); reset question_index and score to zero; swap UI to quiz view | Must | Complete |
| Add random.shuffle() for question order | Import random module; call random.shuffle(filtered_questions) before quiz begins to randomise order each session | Must | Complete |
| Implement show_question() | Display question text with progress counter ('Q 2/6: ...'); store current_answer; clear answer entry box and status bar | Must | Complete |
| Implement check_answer() | Read and strip user input; compare to current_answer with .lower(); increment score on correct; reveal answer on incorrect; block empty submission | Must | Complete |
| Implement next_question() | Increment question_index; detect end of quiz; display final score ('Done! Score: X/Y'); show 'Quiz complete!' in question label | Must | Complete |
| Add input validation to check_answer() | Prevent check_answer() from running if the answer entry box is empty; display 'Type an answer first.' message | Must | Complete |
| Final code review and commenting | Add comprehensive inline comments to all functions; ensure all code is readable and ready for showcase demonstration | Must | Complete |

### Sprint Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|-----------|
| Running out of time before submission | High | High | Sprint 3 ends on submission deadline; all Must Have items prioritised and completed first |
| Quiz logic bugs | Medium | High | Each function tested individually before integration; edge cases (empty input, last question) tested explicitly |

### Sprint Review Report

#### Completed Items

| Item | Status | Notes |
|------|--------|-------|
| start_quiz() filters by category and shuffles questions | Complete | Tested with both AI and Cyber Security categories; shuffle confirmed on repeat runs |
| show_question() displays question with counter | Complete | Format 'Q 1/6: What does VPN stand for?' displays correctly throughout quiz |
| check_answer() validates case-insensitively and blocks empty input | Complete | Correct, wrong, and empty inputs all handled with appropriate status bar messages |
| next_question() advances correctly and detects quiz end | Complete | Final score displayed correctly; 'Quiz complete!' shown in question label |
| Score resets to zero on each new quiz | Complete | Confirmed by running the same quiz twice consecutively |
| Code commented throughout and ready for showcase | Complete | All functions have inline comments explaining logic; code reviewed for readability |
| Portfolio and code submitted to DLE by 23 April 2026 | Complete | All files uploaded individually as per module requirements |

#### Incomplete / Carry-Forward Items

All planned items were completed by the submission deadline. The Manage Flashcards feature (edit and delete) was implemented ahead of schedule and carried into the final sprint for showcase preparation.

#### Items to Address in Next Sprint

Prepare for the showcase on 6 May 2026: practise the 6-minute demonstration, ensure the application runs cleanly on the presentation machine, and be prepared to explain all code sections to the marking panel.

#### Stakeholder Feedback and Product Backlog Adaptations

End-to-end quiz testing was conducted using both available categories. A peer tester confirmed the application was usable and completed all six validation tasks successfully, providing confirmation that the software meets user needs.

---

## Sprint 4 — Showcase Preparation

**Sprint dates:** 24 April 2026 – 6 May 2026  
**Sprint goal:** Prepare for the showcase on 6 May 2026 — practise the 6-minute demonstration, ensure the application runs cleanly on the presentation machine, and be ready to explain all code sections to the marking panel.
