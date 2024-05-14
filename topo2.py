from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.topo import Topo 

 
class MyTopo( Topo ):  
    "Simple topology example."
    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
	
	net = Mininet(controller=RemoteController)

    	info( '*** Adding controllers\n' )
    	cA = net.addController('cA', controller=RemoteController, ip="127.0.0.1", port=6633)
    	cB = net.addController('cB', controller=RemoteController, ip="127.0.0.1", port=6634)
	
	info( '*** Adding hosts\n' )
    	AAh1 = self.addHost('AAh1', ip='10.1.1.1', mac='0A:0A:00:00:00:01')
    	AAh2 = self.addHost('AAh2', ip='10.1.1.2', mac='0A:0A:00:00:00:02')
    	ABh1 = self.addHost('ABh1', ip='10.1.2.1', mac='0A:0B:00:00:00:01')
    	ABh2 = self.addHost('ABh2', ip='10.1.2.2', mac='0A:0B:00:00:00:02')
    	BAh1 = self.addHost('BAh1', ip='10.10.10.1', mac='0A:0B:0A:00:00:01')
   	BAh2 = self.addHost('BAh2', ip='10.10.10.2', mac='0A:0B:0A:00:00:02')
    	BBh1 = self.addHost('BBh1', ip='10.10.20.1', mac='0A:0B:0B:00:00:01')
    	BBh2 = self.addHost('BBh2', ip='10.10.20.2', mac='0A:0B:0B:00:00:02')
        
        
        info( '*** Adding switches\n' )
    	sA = self.addSwitch( 's1', dpid='0000000000000001' )     #Add dpid as string containing a 16 byte (0 padded) hex equivalent of the int dpid 
    	sAA = self.addSwitch( 's11', dpid='000000000000000b' )
    	sAB = self.addSwitch( 's12', dpid='000000000000000c' )
    	sB = self.addSwitch( 's2', dpid='0000000000000002' )
    	sBA = self.addSwitch( 's21', dpid='0000000000000015' )
    	sBB = self.addSwitch( 's22', dpid='0000000000000016' )
    
    	info( '*** Adding links\n' )
    	self.addLink(AAh1,sAA)
    	self.addLink(AAh2,sAA)
    
    	self.addLink(ABh1,sAB)
    	self.addLink(ABh2,sAB)
    
    	self.addLink(BAh1,sBA)
    	self.addLink(BAh2,sBA)
    
    	self.addLink(BBh1,sBB)
    	self.addLink(BBh2,sBB)

    	self.addLink(sAA,sA)
    	self.addLink(sAB,sA)
    
    	self.addLink(sBA,sB)
    	self.addLink(sBB,sB)
    
    	self.addLink(sA,sB)


    	info('*** Starting network\n')
    	#net.build()
    	#sA.start([cA])
    	#sAA.start([cA])
    	#sAB.start([cA])
    	#sB.start([cB])
    	#sBA.start([cB])
    	#sBB.start([cB])
topos = { 'mytopo': ( lambda: MyTopo() ) }  
