#HTTP traffic from H1 -> H2
sudo ovs-ofctl add-flow s1 in_port=1,priority=65535,dl_type=0x0800,nw_proto=6,tcp_dst=80,action=output:2
sudo ovs-ofctl add-flow s2 in_port=1,priority=65535,dl_type=0x0800,nw_proto=6,tcp_dst=80,action=output:2
sudo ovs-ofctl add-flow s4 in_port=1,priority=65535,dl_type=0x0800,nw_proto=6,tcp_dst=80,action=output:2
#HTTP traffic from H2 -> H1
sudo ovs-ofctl add-flow s1 in_port=3,priority=65535,dl_type=0x0800,nw_proto=6,tcp_src=80,action=output:1
sudo ovs-ofctl add-flow s3 in_port=2,priority=65535,dl_type=0x0800,nw_proto=6,tcp_src=80,action=output:3
sudo ovs-ofctl add-flow s4 in_port=2,priority=65535,dl_type=0x0800,nw_proto=6,tcp_src=80,action=output:4
#other traffic from h1->h2
sudo ovs-ofctl add-flow s1 in_port=1,actions=output:3
sudo ovs-ofctl add-flow s3 in_port=3,actions=output:1
sudo ovs-ofctl add-flow s5 in_port=3,actions=output:2
sudo ovs-ofctl add-flow s4 in_port=3,actions=output:2
#other traffic from h2 -> h1
sudo ovs-ofctl add-flow s4 in_port=2,actions=output:1
sudo ovs-ofctl add-flow s2 in_port=2,actions=output:3
sudo ovs-ofctl add-flow s5 in_port=1,actions=output:3
sudo ovs-ofctl add-flow s3 in_port=1,actions=output:3
sudo ovs-ofctl add-flow s1 in_port=3,actions=output:1
