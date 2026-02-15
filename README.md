<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Smart Revision Planner] 🎯

## Basic Details

### Team Name: [DEVIKRISHNA S]

### Team Members
- Member 1: [DEVIKRISHNA S] - [Saintgits College of Engineering Pathamuttom Kottayam]
- Member 2: [Name] - [College]

### Hosted Project Link
[http://127.0.0.1:5000/]

### Project Description
[Smart Revision Planner: A web application that helps students plan their exam preparation efficiently. Users can input subjects, chapters, and difficulty levels, and the planner calculates daily study targets, priorities, and recommended study time, with optional AI-generated study tips and motivation.]

### The Problem statement
[Students often struggle to manage their time effectively while preparing for exams. They find it difficult to prioritize subjects, estimate daily study goals, and stay motivated, leading to inefficient revision and stress.]

### The Solution
[The Smart Revision Planner is a web-based tool that helps students organize their study schedule. By entering subjects, number of chapters, and difficulty levels, the planner calculates daily study targets, prioritizes subjects, recommends study time, and optionally provides AI-generated study tips and motivational guidance. This ensures structured, efficient, and motivated preparation for exams.]

---

## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: [ Python, html]
- Frameworks used: [flask]
- Libraries used: [Flask,openai,math,os]
- Tools used: [VS Code, Git, GitHub, Python, Web Browser]

**For Hardware:**
- Main components: [Flask Backend,HTML/CSS Frontend,AI Mentor Module,Calculation Engine]
- Specifications: [Programming Language,Web Framework,AI Model,Browser Compatibility,Data Input,output]
- Tools required: [VS Code,Python 3.x,Flask library,OpenAI Python library,Git,Github,Web Browser]

OpenAI Python library

Git (for version control)

GitHub (for remote repository)




---

## Features

List the key features of your project:
- Feature 1: [Description]
- Feature 2: [Description]
- Feature 3: [Description]
- Feature 4: [Description]

---

## Implementation

### For Software:

#### Installation
```bash
[Installation commands - e.g., npm install, pip install -r requirements.txt]
```

#### Run
```bash
[Run commands - e.g., npm start, python app.py]
```

### For Hardware:

#### Components Required
[List all components needed with specifications]

#### Circuit Setup
[Explain how to set up the circuit]

---

## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

![Screenshot1](<img width="1366" height="768" alt="1" src="https://github.com/user-attachments/assets/87258843-a4ba-4c0d-a115-db6cc5c7f7e2" />
)
*Shows the backend logic for the Smart Revision Planner, including AI suggestions, study plan calculations, and priority evaluation*

![Screenshot2](<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b47d57eb-0881-497d-955c-d0f93c5a4b53" />
)
*Shows the backend logic for the Smart Revision Planner, including AI suggestions, study plan calculations, and priority evaluation*

![Screenshot3](<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/a4247ce8-18c1-46f4-8f8b-db4c5a0e8862" />
)
*Shows the frontend interface where users enter exam details and view their personalized study plan.*

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

**Application Workflow:**

![Workflow](docs/workflow.png)
*Add caption explaining your workflow*

---

### For Hardware:

#### Schematic & Circuit

![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

#### Build Photos

![Team](Add photo of your team here)

![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** `https://api.yourproject.com`

##### Endpoints

**GET /api/endpoint**
- **Description:** [What it does]
- **Parameters:**
  - `param1` (string): [Description]
  - `param2` (integer): [Description]
- **Response:**
```json
{
  "status": "success",
  "data": {}
}
```

**POST /api/endpoint**
- **Description:** [What it does]
- **Request Body:**
```json
{
  "field1": "value1",
  "field2": "value2"
}
```
- **Response:**
```json
{
  "status": "success",
  "message": "Operation completed"
}
```

[Add more endpoints as needed...]

---

### For Mobile Apps:

#### App Flow Diagram

![App Flow](docs/app-flow.png)
*Explain the user flow through your application*

#### Installation Guide

**For Android (APK):**
1. Download the APK from [Release Link]
2. Enable "Install from Unknown Sources" in your device settings:
   - Go to Settings > Security
   - Enable "Unknown Sources"
3. Open the downloaded APK file
4. Follow the installation prompts
5. Open the app and enjoy!

**For iOS (IPA) - TestFlight:**
1. Download TestFlight from the App Store
2. Open this TestFlight link: [Your TestFlight Link]
3. Click "Install" or "Accept"
4. Wait for the app to install
5. Open the app from your home screen

**Building from Source:**
```bash
# For Android
flutter build apk
# or
./gradlew assembleDebug

# For iOS
flutter build ios
# or
xcodebuild -workspace App.xcworkspace -scheme App -configuration Debug
```

---

### For Hardware Projects:

#### Bill of Materials (BOM)

| Component | Quantity | Specifications | Price | Link/Source |
|-----------|----------|----------------|-------|-------------|
| Arduino Uno | 1 | ATmega328P, 16MHz | ₹450 | [Link] |
| LED | 5 | Red, 5mm, 20mA | ₹5 each | [Link] |
| Resistor | 5 | 220Ω, 1/4W | ₹1 each | [Link] |
| Breadboard | 1 | 830 points | ₹100 | [Link] |
| Jumper Wires | 20 | Male-to-Male | ₹50 | [Link] |
| [Add more...] | | | | |

**Total Estimated Cost:** ₹[Amount]

#### Assembly Instructions

**Step 1: Prepare Components**
1. Gather all components listed in the BOM
2. Check component specifications
3. Prepare your workspace
![Step 1](images/assembly-step1.jpg)
*Caption: All components laid out*

**Step 2: Build the Power Supply**
1. Connect the power rails on the breadboard
2. Connect Arduino 5V to breadboard positive rail
3. Connect Arduino GND to breadboard negative rail
![Step 2](images/assembly-step2.jpg)
*Caption: Power connections completed*

**Step 3: Add Components**
1. Place LEDs on breadboard
2. Connect resistors in series with LEDs
3. Connect LED cathodes to GND
4. Connect LED anodes to Arduino digital pins (2-6)
![Step 3](images/assembly-step3.jpg)
*Caption: LED circuit assembled*

**Step 4: [Continue for all steps...]**

**Final Assembly:**
![Final Build](images/final-build.jpg)
*Caption: Completed project ready for testing*

---

### For Scripts/CLI Tools:

#### Command Reference

**Basic Usage:**
```bash
python script.py [options] [arguments]
```

**Available Commands:**
- `command1 [args]` - Description of what command1 does
- `command2 [args]` - Description of what command2 does
- `command3 [args]` - Description of what command3 does

**Options:**
- `-h, --help` - Show help message and exit
- `-v, --verbose` - Enable verbose output
- `-o, --output FILE` - Specify output file path
- `-c, --config FILE` - Specify configuration file
- `--version` - Show version information

**Examples:**

```bash
# Example 1: Basic usage
python script.py input.txt

# Example 2: With verbose output
python script.py -v input.txt

# Example 3: Specify output file
python script.py -o output.txt input.txt

# Example 4: Using configuration
python script.py -c config.json --verbose input.txt
```

#### Demo Output

**Example 1: Basic Processing**

**Input:**
```
This is a sample input file
with multiple lines of text
for demonstration purposes
```

**Command:**
```bash
python script.py sample.txt
```

**Output:**
```
Processing: sample.txt
Lines processed: 3
Characters counted: 86
Status: Success
Output saved to: output.txt
```

**Example 2: Advanced Usage**

**Input:**
```json
{
  "name": "test",
  "value": 123
}
```

**Command:**
```bash
python script.py -v --format json data.json
```

**Output:**
```
[VERBOSE] Loading configuration...
[VERBOSE] Parsing JSON input...
[VERBOSE] Processing data...
{
  "status": "success",
  "processed": true,
  "result": {
    "name": "test",
    "value": 123,
    "timestamp": "2024-02-07T10:30:00"
  }
}
[VERBOSE] Operation completed in 0.23s
```

---

## Project Demo

### Video
[https://drive.google.com/file/d/1tmyN3WQczp9lMmKMRICj_9ePWx6aGNcL/view?usp=drive_link]

*Explain what the video demonstrates - key features, user flow, technical highlights*

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
-Assisted in writing Flask backend code and HTML frontend templates.

-Generated logic for study planner calculations and result display.

-Helped debug code errors and improve readability

**Key Prompts Used:**
-"Create a Flask route to handle form submissions and calculate study plan"

-"Generate HTML template to display subjects, chapters per day, and study time"

-"Fix Python code that isn’t updating results correctly in Flask"

**Percentage of AI-generated code:** [Approximately 80%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - Frontend,UI design, React components]
- [Name 2]: [Specific contributions - Backend,API integration, DB setup]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
