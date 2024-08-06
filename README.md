# Network Task Automator

 <div align="center">
<img width="809" alt="Screenshot 2024-08-06 at 2 28 11 PM" src="https://github.com/user-attachments/assets/eba38530-2912-401f-abd0-5c9e85767303">
 </div>
 
## Key Features:

### 1. Multithreaded server:

The server for the Network Task Automator project operates on a multithreaded architecture, with each task assigned a unique port and socket for optimized performance. A dedicated thread manages each specific task, ensuring efficient and responsive task execution.

### 2. Home Page: 

 This page displays the main interface of the Network Task Automator, featuring a colorful grid layout with each tile representing a different functionality. 

 <div align="center">
<img width="413" alt="Screenshot 2024-08-06 at 2 09 37 PM" src="https://github.com/user-attachments/assets/79352d0e-101d-4113-9f55-f91c5ea26b99">
 </div>
 
 This design allows for quick access to the various tasks the tool can perform, enhancing user navigation and efficiency.

### 3. Image Convertor:

- Input Reception: The server receives the following inputs from the user:

  - Image Name: The name of the image to be converted.
    
  - Image Path: The location where the image is stored.
    
  - Image Format: The desired format to which the image should be converted.

- Image Conversion Process:The server decodes the user inputs and converts the image to the specified format.

- Image Management: After conversion, the original image is removed from the system.
  
- Port Assignment: This entire process is managed through a specific port, to handle image conversion tasks.

 <div align="center">
<img width="445" alt="Screenshot 2024-08-06 at 2 14 31 PM" src="https://github.com/user-attachments/assets/a3e03d56-7842-440a-b0d9-6bb7255b22fe">
 </div>

### 4. Rename File:

- User Input: The user provides two pieces of information:

  - Old File Name: The current name of the file.
    
  - New File Name: The desired new name for the file.
    
- Operation: Upon receiving the old and new filenames, the server processes the rename command through a port dedicated specifically for file renaming operations.

 <div align="center">
<img width="440" alt="Screenshot 2024-08-06 at 2 17 32 PM" src="https://github.com/user-attachments/assets/d5b16a40-058d-4433-95d7-adcc5cee5556">
 </div>

### 5. Download Audio/Video:

This function enables users to download audio or video files by entering the file name in the provided input field and clicking the "Download" button.

 <div align="center">
<img width="441" alt="Screenshot 2024-08-06 at 2 21 36 PM" src="https://github.com/user-attachments/assets/e76a2cf3-d5da-4831-ac67-a0876bc625d0">
 </div>

 ### 6. Network Statistics:

 This feature allows users to check the status of specific network ports.

 - Function: The screen provides a button labeled "SCAN!" which, when clicked, triggers the server to perform a scan of predefined port ranges using the nmapScanner tool.
   
- Output Display: The results of the scan are displayed directly on the screen, indicating whether individual ports (such as port 20, 21, 22, 23, 24, and 25) are open or closed.
  
- Data Storage: After the scan, the results are saved in a file named "stat_data," which logs the status of each port for record-keeping and further analysis.

 <div align="center">
<img width="440" alt="Screenshot 2024-08-06 at 2 24 01 PM" src="https://github.com/user-attachments/assets/f63f725f-ef84-4816-990b-a27a373c7a09">
 </div>

 ### 7. Network Alarm:

 Network Alarm is designed to check the status of network ports.

- Input Field: Users can input a specific port number they wish to check.

- Scan Button: A "SCAN!" button initiates the scan using the nmap port scanner tool.

- Status Display: The result of the scan, such as "PORT 21 is open," is displayed, informing the user whether the specified port is open or closed.

 <div align="center">
   <img width="439" alt="Screenshot 2024-08-06 at 2 26 58 PM" src="https://github.com/user-attachments/assets/a8f1d04b-b002-4ccf-b96e-70eac7aaab96">
  </div>

 ### 8. Network Configuration:
 
 - Dynamic IP Assignment: The server automatically assigns IP addresses to clients, modeled after the Dynamic Host Configuration Protocol (DHCP).
   
 - Client Interaction: Users can view and retrieve the IP address for each client machine, as demonstrated below for Client1, Client2, and Client3, with assigned IP addresses such as 192.168.174.2, 192.168.174.3, and 192.168.174.4 respectively.
   
  <div align="center">
 <img width="504" alt="Screenshot 2024-08-06 at 2 31 53 PM" src="https://github.com/user-attachments/assets/e8f1fd9b-26de-4373-9349-af79e43fee59">
  </div>

### 9. Network Equations:

- Input Fields: Users can input values for parameters that affect transmission delay and propagation delay. These include data size, bandwidth for transmission delay, and distance, signal speed for propagation delay.

- Calculation Buttons:

  - "calculate transmission delay" uses the user-provided data size and bandwidth to compute the time it takes for data to be transmitted across a network.
  - "calculate Prop delay" computes the time taken for a signal to travel from the source to the destination using the distance and signal speed.
  - "calculate Total delay" adds both the transmission and propagation delays to provide a comprehensive view of total network delay.

- Results Display: Each calculation provides a numeric output displayed on the interface, offering clear and immediate feedback on network delays.

  <div align="center">
  <img width="457" alt="Screenshot 2024-08-06 at 2 38 02 PM" src="https://github.com/user-attachments/assets/f1aa0a38-4639-4e2f-a235-6c56ba1bd07b">
 </div>
