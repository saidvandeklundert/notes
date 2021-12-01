extern crate ipnet;
use ipnet::Ipv4Subnets;
use ipnet::{IpNet, Ipv4Net, Ipv6Net};
use std::net::{Ipv4Addr, Ipv6Addr};
use std::str::FromStr;
fn main() {
    {
        let start = Ipv4Addr::new(10, 0, 0, 0);
        let end = Ipv4Addr::new(10, 0, 0, 239);

        println!("\n/0 or greater subnets between {} and {}:", start, end);

        // Output all subnets starting with the largest that will fit. This
        // will give us the smallest possible set of valid subnets.
        //
        // Output:
        //  subnet 0 = 10.0.0.0/25
        //  subnet 1 = 10.0.0.128/26
        //  subnet 2 = 10.0.0.192/27
        //  subnet 3 = 10.0.0.224/28

        let subnets = Ipv4Subnets::new(start, end, 0);

        for (i, n) in subnets.enumerate() {
            println!("\tsubnet {} = {}", i, n);
        }

        println!("\n/26 or greater subnets between {} and {}:", start, end);

        // Output all subnets with prefix lengths less than or equal to 26.
        // This results in more subnets, but limits them to a maximum size.
        //
        // Output:
        //  subnet 0 = 10.0.0.0/26
        //  subnet 1 = 10.0.0.64/26
        //  subnet 2 = 10.0.0.128/26
        //  subnet 3 = 10.0.0.192/27
        //  subnet 4 = 10.0.0.224/28

        let subnets = Ipv4Subnets::new(start, end, 26);

        for (i, n) in subnets.enumerate() {
            println!("\tsubnet {} = {}", i, n);
        }
    }
    {
        // Create an Ipv4Net and Ipv6Net from their constructors.

        let net4 = Ipv4Net::new(Ipv4Addr::new(10, 1, 1, 0), 24).unwrap();
        let net6 = Ipv6Net::new(Ipv6Addr::new(0xfd, 0, 0, 0, 0, 0, 0, 0), 24).unwrap();

        // They can also be created from string representations.

        let net4 = Ipv4Net::from_str("10.1.1.0/24").unwrap();
        let net6 = Ipv6Net::from_str("fd00::/24").unwrap();

        // Or alternatively as follows.

        let net4: Ipv4Net = "10.1.1.0/24".parse().unwrap();
        let net6: Ipv6Net = "fd00::/24".parse().unwrap();

        // IpNet can represent either an IPv4 or IPv6 network address.

        let net = IpNet::from(net4);

        // It can also be created from string representations.

        let net = IpNet::from_str("10.1.1.0/24").unwrap();
        let net: IpNet = "10.1.1.0/24".parse().unwrap();

        // There are a number of methods that can be used. Read the
        // documentation for the full details.

        println!("{} hostmask = {}", net, net.hostmask());
        println!("{} netmask = {}", net4, net4.netmask());
    }
    {
        // Example input list of overlapping and adjacent prefixes.

        let strings = vec![
            "10.0.0.0/20",
            "10.0.0.0/24",
            "10.0.1.0/24",
            "10.0.1.1/24",
            "10.0.1.2/24",
            "10.0.2.0/24",
            "10.1.0.0/24",
            "10.1.1.0/24",
            "fd00::/32",
            "fd00:1::/32",
        ];

        let nets: Vec<IpNet> = strings.iter().filter_map(|p| p.parse().ok()).collect();

        println!("\nAggregated IP prefixes:");

        // Output:
        //  10.0.0.0/23
        //  10.0.2.0/24
        //  10.1.0.0/23
        //  192.168.0.0/22
        //  fd00::/31

        for n in IpNet::aggregate(&nets) {
            println!("\t{}", n);
        }
    }
}
