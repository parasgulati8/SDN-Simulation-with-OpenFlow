# SDN-Simulation-with-OpenFlow
Use Mininet to create topologies with OpenFlow switches and install flows to simulate network operations

MiniNet creates scalable Software-Defined Networks (up to hundreds of nodes) using OpenFlow, on a single PC. 
It allows to quickly create, interact with and customize a software defined network prototype with complex topologies, and can be used to emulate real networks – all on your PC
MiniNet can work with any kind of OpenFlow controller

<h2>Simple SDN Topology</h2>

Simulating a software defined network with 2 hosts and 5 switches using mininet and OpenFlow switches.
![Topology_1](https://user-images.githubusercontent.com/43897597/54611023-90363980-4a2c-11e9-8b15-d08757ced127.PNG)

Used Mininet to create the topology above, where A, B, C, D, and E are all Openflow switches.
Enforced the following policies so that,

Traffic from H1 -> H2
    <li>HTTP traffic with d_port=80 follows path: A-B-D</li>
    <li>other traffic follows path: A-C-E-D</li>

Traffic from H2 -> H1
    <li>HTTP traffic with s_port=80, follow path: D-C-A</li>
    <li>other traffic, follow path: D-B-E-C-A</li>


<h2>Fat-Tree topology in Mininet</h2>
Installed OpenFlow switches, hosts and links in the below fashion to create a N=4 Fat-Tree topology. 
<div style="text-align:center"><img src ="https://user-images.githubusercontent.com/43897597/54611230-f458fd80-4a2c-11e9-918a-6861eb70ac2e.PNG" width="700" height="300"/></div>


Installed OpenFlow switches, hosts and links in the below fashion to create a N=6 Fat-Tree topology
<div style="text-align:center"><img src ="https://user-images.githubusercontent.com/43897597/54611239-f7ec8480-4a2c-11e9-87d9-a799df128919.PNG" width="700" height="300"/></div>


<h2>Installation</h2>

The code for simple SDN topology is in "topology.py". First you need to create the topology with the python script.
But the packets will not flow until you install the flows in the switches. The flows for this topology are in shell script "Flows.sh". You can run the shell script in a separate terminal to install the flows.

Then run the ping command in mininet to test the network. If the packets are dropped, that means the flows are not installed in controller and hence the switches do not know how to handle the packets.

After successfully installing the flows, you can run the wireshark and capture the packets flowing in the network to check the flows.
The code for Fat Tree topologies are present in "FatTree_4.py" and "FatTree_6.py". There are no flows in FatTree networks. However you can easily install the flows using commands similar to previous topology.
