"""Custom topology example
Two directly connected switches plus a host for each switch:
   host --- switch --- switch --- host
Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        ovsA = self.addSwitch( 's1' )
        ovsB = self.addSwitch( 's2' )
        ovsC = self.addSwitch( 's3' )
        ovsD = self.addSwitch( 's4' )
        ovsE = self.addSwitch( 's5' )

        # Add links
        self.addLink(h1, ovsA)
        self.addLink(ovsA, ovsB)
        self.addLink(ovsB, ovsD)
        self.addLink(ovsD, h2)
        self.addLink( ovsB,	ovsE)
        self.addLink(ovsE ,	ovsD)
        self.addLink(ovsE, ovsC)
        self.addLink(ovsC,ovsD)
        self.addLink( ovsC, ovsA	)
        #self.addLink( BSwitch, ESwitch	)
        #self.addLink( CSwitch, ESwitch	)
        #self.addLink( DSwitch, rightHost)

topos = { 'mytopo': ( lambda: MyTopo() ) }
