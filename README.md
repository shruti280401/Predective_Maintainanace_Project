# Predective_Maintainanace_Project
## Predective Maintainance of Gas Turbine Component Degradation in Naval Vessels
Predictive maintenance is a strategy used to anticipate when equipment or machinery is likely to fail so that maintenance can be performed just in time to address issues before they lead to a breakdown. This approach relies on various data sources and techniques to monitor the condition and performance of equipment in real time or at regular intervals.

This application aims to predict the <b>failure of gas turbine components in naval vessels for predictive maintenance</b> using machine learning techniques. It employs a synthetic dataset and is built using a Random Forest model to assess the likelihood of component failure based on various input parameters. The research adopts a mixed-methods approach, incorporating both quantitative data from surveys and the <b>Random Forest model</b> to enhance prediction accuracy and maintenance strategies.

You can view the deployed app here :[Predective maintaianace of Gas Turbine](https://predectivemaintainanaceproject-uw4zzsvbqydsh2lgxbc56d.streamlit.app/?embed_options=dark_theme)

##Dataset Description
  The dataset consist of following features:
  "Lever position (lp) [ ]"
  "Ship speed (v) [knots]"
  "Gas Turbine shaft torque (GTT) [kN m]"
  "Gas Turbine rate of revolutions (GTn) [rpm]"
  "Gas Generator rate of revolutions (GGn) [rpm]"
  "Starboard Propeller Torque (Ts) [kN]"
  "Port Propeller Torque (Tp) [kN]"
  "HP Turbine exit temperature (T48) [C]"
  "GT Compressor inlet air temperature (T1) [C]"
  "GT Compressor outlet air temperature (T2) [C]"
  "HP Turbine exit pressure (P48) [bar]"
  "GT Compressor inlet air pressure (P1) [bar]"
  "GT Compressor outlet air pressure (P2) [bar]"
  "Gas Turbine exhaust gas pressure (Pexh) [bar]"
  "Turbine Injection Control (TIC) [%]"
  "Fuel flow (mf) [kg/s]"
  "GT Turbine decay state coefficient."

## Running the Application
  Navigate to the cloned repository in your terminal or command prompt, then run the following command:
      streamlit run app.py
 This will launch the application in your web browser.

## Application Workflow
   1) Upon launching the application, you will see an input form with various fields corresponding to the features in the dataset.
  2)Provide the required inputs in the form. Select provide Gas Generator rate of revolutions (GGn) in rpm,HP Turbine exit temperature (T48) in [C],Gas Turbine exhaust gas pressure (Pexh) in bar.
  3)Click on the "Predict Failure" button to make a prediction.
  The application will display whether the machine is predicted to experience failure or not.

## Authors
- [Shruti Gumgaonkar](https://github.com/shruti280401)
 

