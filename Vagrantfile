#
# Juniper lab v0.1
#
# ge-0/0/0.0: management interface
# ge-0/0/1.0 - ge-0/0/7.0: user interfaces

Vagrant.configure(2) do |config|
#  config.vm.box = "jlk0013/vMX_12.1R1.9"
  config.vm.box = "juniper/vqfx10k-re"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 512 
    vb.cpus = 2
    vb.gui = false
  end

  config.vm.define "vsrx1" do |vsrx1|
    vsrx1.vm.host_name = "vsrx1"
    vsrx1.vm.network "private_network",
                     ip: "10.99.12.1",
                     virtualbox__intnet: "1-2"
    vsrx1.vm.network "private_network",
                     ip: "10.99.13.1",
                     virtualbox__intnet: "1-3"
    config.ssh.insert_key = false
    config.vm.network "forwarded_port", guest: 22, host: 22221, id: "ssh"
  end

  config.vm.define "vsrx2" do |vsrx2|
    vsrx2.vm.host_name = "vsrx2"
    config.vm.network "forwarded_port", guest: 22, host: 22222, id: "ssh"
    vsrx2.vm.network "private_network",
                     ip: "10.99.23.2",
                     virtualbox__intnet: "2-3"
    vsrx2.vm.network "private_network",
                     ip: "10.99.12.2",
                     virtualbox__intnet: "1-2"
    config.ssh.insert_key = false
  end

  config.vm.define "vsrx3" do |vsrx3|
    vsrx3.vm.host_name = "vsrx3"
    config.vm.network "forwarded_port", guest: 22, host: 22223, id: "ssh"
    vsrx3.vm.network "private_network",
                     ip: "10.99.13.3",
                     virtualbox__intnet: "1-3"
    vsrx3.vm.network "private_network",
                     ip: "10.99.23.3",
                     virtualbox__intnet: "2-3"
    vsrx3.vm.network "private_network",
                     ip: "10.99.34.3",
                     virtualbox__intnet: "3-4"
    config.ssh.insert_key = false
  end

  config.vm.define "vsrx4" do |vsrx4|
    vsrx4.vm.host_name = "vsrx4"
    config.vm.network "forwarded_port", guest: 22, host: 22224, id: "ssh"
    vsrx4.vm.network "private_network",
                      ip: "10.99.34.4",
                      virtualbox__intnet: "3-4"
    config.ssh.insert_key = false
  end
end

# config.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
# config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
# config.ssh.username = "vagrant"
# config.ssh.password = "vagrant"
