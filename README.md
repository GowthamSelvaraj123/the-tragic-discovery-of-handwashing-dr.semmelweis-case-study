<h1>The Tragic Discovery of Handwashing – Dr. Semmelweis</h1>
    <h2>Project Overview</h2>
    <p>
        This project analyzes historical maternal mortality data from the Vienna General Hospital during the 1840s.
        It examines monthly and yearly births and deaths in two clinics:
        <strong>Clinic 1</strong> (male doctors and medical students) and 
        <strong>Clinic 2</strong> (female midwives).
    </p>    
    <h2>Objectives</h2>
    <ul>
        <li>Explore and clean the datasets for preliminary analysis.</li>
        <li>Visualize monthly births and deaths using Matplotlib.</li>
        <li>Compare yearly births and deaths between clinics using Plotly.</li>
        <li>Calculate and visualize maternal mortality rates per clinic.</li>
        <li>Understand the historical significance of Dr. Semmelweis’ discovery of handwashing.</li>
    </ul>
  
  <h2>Datasets</h2>
    <ul>
        <li><code>monthly_deaths.csv</code> – Contains monthly births and deaths from 1841–1849.</li>
        <li><code>annual_deaths_by_clinic.csv</code> – Contains yearly births and deaths for Clinic 1 and Clinic 2.</li>
    </ul>    
    <h2>Project Structure</h2>
    <pre>
    /day-80-the-tragic-discovery-of-handwashing/
    ├── app.py
    ├── monthly_deaths.csv
    ├── annual_deaths_by_clinic.csv
    ├── README.html
    └── .venv/
    </pre>
    <h2>How to Run</h2>
    <p>
        1. Clone the repository:<br>
        <code>git clone &lt;repo-url&gt;</code><br>
        2. Navigate to the project folder and activate the virtual environment:<br>
        <code>.venv\Scripts\activate</code><br>
        3. Install dependencies:<br>
        <code>pip install pandas matplotlib seaborn plotly scipy</code><br>
        4. Run the analysis script:<br>
        <code>python app.py</code>
    </p>
    <h2>Key Insights</h2>
    <ul>
        <li>Clinic 1 had more births and higher maternal mortality than Clinic 2.</li>
        <li>Average death rate in Clinic 1: ~9.92%, Clinic 2: ~3.88%.</li>
        <li>Sharp drop in deaths after 1847 corresponds to the adoption of handwashing practices.</li>
        <li>Dr. Semmelweis’ discovery highlights the importance of hygiene in preventing childbed fever.</li>
    </ul>
    <h2>Visualizations</h2>
    <ul>
        <li>Monthly births and deaths (Matplotlib)</li>
        <li>Yearly births and deaths by clinic (Plotly)</li>
        <li>Percentage of deaths per clinic over time (Plotly)</li>
    </ul>
    <h2>Author</h2>
    <p>Gowtham S – Web & Data Analysis Enthusiast</p>
