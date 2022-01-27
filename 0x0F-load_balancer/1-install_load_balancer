#!/usr/bin/env bash                                                           
# Install and configure HAproxy on your lb-01 server                          
sudo apt-get update
sudo apt-get -y install software-properties-common
sudo add-apt-repository -y ppa:vbernat/haproxy-1.8
sudo apt-get update
sudo apt-get -y install haproxy=1.8.\*
options="\n\tbind :80\n\tmode http\n\tuse_backend mybackend\nbackend mybackend\n\tbalance roundrobin\n\tserver 971-web-01 34.236.171.16:80 check\n\tserver 971-web-02 3.236.14.41:80 check"
sed -i '/errorfile 504/a frontend myconf' /etc/haproxy/haproxy.cfg
sed -i "s/frontend myconf/&$options/g" /etc/haproxy/haproxy.cfg
sudo service haproxy restart
