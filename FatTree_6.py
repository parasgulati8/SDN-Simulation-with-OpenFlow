"""Custom topology example
Two directly connected switches plus a host for each switch:
host --- switch --- switch --- host
Adding the 'topos' dict with a key/value
pair to generate our newly defined topology enables one to pass 
in '--topo=mytopo' from the command line""" 

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

     def build( self ):
         "Create custom topo."
         
         # Add hosts and switches
         H1 = self.addHost( 'h1')
         H2 =  self.addHost( 'h2' )
         H3 =  self.addHost( 'h3' )
         H4 =  self.addHost( 'h4' )
         H5 =  self.addHost( 'h5' )
         H6 =  self.addHost( 'h6' )
         H7 =  self.addHost( 'h7' )
         H8 =  self.addHost( 'h8' )
         H9 =  self.addHost( 'h9' )
         H10 =  self.addHost( 'h10' )
         H11 =  self.addHost( 'h11' )
         H12 =  self.addHost( 'h12' )
         H13 =  self.addHost( 'h13' )
         H14 =  self.addHost( 'h14' )
         H15 =  self.addHost( 'h15' )
         H16 =  self.addHost( 'h16' )
         H17 =  self.addHost( 'h17' )
         H18 =  self.addHost( 'h18' )

         s1 = self.addSwitch( 's1' )
         s2 = self.addSwitch( 's2' )
         s3 = self.addSwitch( 's3' )
         s4 = self.addSwitch( 's4' )
         s5 = self.addSwitch( 's5' )
         s6 = self.addSwitch( 's6' )
         s7 = self.addSwitch( 's7' )
         s8 = self.addSwitch( 's8' )
         s9 = self.addSwitch( 's9' )

        #Add Links
         self.addLink( H1, s1 )
         self.addLink( H2, s1 )
         self.addLink( H3, s1 )
         self.addLink( H4, s2 )
         self.addLink( H5, s2 )
         self.addLink( H6, s2 )
         self.addLink( H7, s3 )
         self.addLink( H8, s3 )
         self.addLink( H9, s3 )
         self.addLink( H10, s4 )
         self.addLink( H11, s4 ) 
         self.addLink( H12, s4 )
         self.addLink( H13, s5 )
         self.addLink( H14, s5 )
         self.addLink( H15, s5 )
         self.addLink( H16, s6 )
         self.addLink( H17, s6 )
         self.addLink( H18, s6 )
         self.addLink( s1, s7 )
         self.addLink( s1, s8 )
         self.addLink( s1, s9 )
         self.addLink( s2, s7 )
         self.addLink( s2, s8 )
         self.addLink( s2, s9 )
         self.addLink( s3, s7 )
         self.addLink( s3, s8 )
         self.addLink( s3, s9 )
         self.addLink( s4, s7 )
         self.addLink( s4, s8 )
         self.addLink( s4, s9 )
         self.addLink( s5, s7 )
         self.addLink( s5, s8 )
         self.addLink( s5, s9 )
         self.addLink( s6, s7 )
         self.addLink( s6, s8 )
         self.addLink( s6, s9 )






         
         

         

    topos = { 'mytopo': ( lambda: MyTopo() ) }
