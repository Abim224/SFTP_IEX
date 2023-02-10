# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 22:35:36 2023

@author: Abinash.m
"""

import streamlit as st
import paramiko
from paramiko.client import SSHClient
import os
# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a file")


hostname = 'luminadatamatics.exavault.com'
username = 'WFM'
password = 'Password@2024'
sshcon   = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no known_hosts error
sshcon.connect(hostname, username=username,password=password)
sftp_client = sshcon.open_sftp()
# If a file is uploaded
source=r"C:\Users\abinash.m\.spyder-py3\IEX_SFTP"

if uploaded_file is not None:
    # Get the file name
    file_name = uploaded_file.name
    
    with open(os.path.join(source,uploaded_file.name),"wb") as f:
        f.write(uploaded_file.getbuffer())
    st.write("File name:", file_name)
    if file_name.startswith('Forecast'):
        # file = '/Forecast/{}'.format(file_name)
        file_path = os.path.join("/Forecast/", uploaded_file.name)
        st.write('Move to forecast folder')
        sftp_client.chdir("/Forecast")
        st.write(sftp_client.getcwd())
        st.write(file_path)
        sftp_client.put("{0}/{1}".format(source,file_name),"/Forecast/{}".format(file_name))
        st.write('Success')
    elif file_name.startswith('Schedule'):
        file_path = os.path.join("/Scheduling/", uploaded_file.name)
        st.write('Move to Scheduling folder')
        sftp_client.chdir("/Scheduling")
        st.write(sftp_client.getcwd())
        st.write(file_path)
        sftp_client.put("{0}/{1}".format(source,file_name),"/Scheduling/{}".format(file_name))
        st.write('Success')
    else:
        file_path = os.path.join("/Other/", uploaded_file.name)
        st.write('Move to Other folder')
        sftp_client.chdir("/Other")
        st.write(sftp_client.getcwd())
        st.write(file_path)
        sftp_client.put("{0}/{1}".format(source,file_name),"/Other/{}".format(file_name))
        st.write('Success')
 # sftp_client.chdir("/Test")
 # sftp_client.put('C:/Users/abinash.m/Documents/ScheduleChanges-1215220217.xml','/Test/ScheduleChanges-1215220217.xml')
