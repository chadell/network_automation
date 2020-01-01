# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.require_version('>= 2.0')
unless Vagrant.has_plugin?('vagrant-vyos')
  system('vagrant plugin install vagrant-vyos') || exit!
end

Vagrant.configure(2) do |config|

  ##### DEFINE VM for routerA #####
  config.vm.define "routerA" do |device|

    device.vm.hostname = "routerA"
    device.vm.box = "higebu/vyos"
    device.vm.box_version = "1.1.7"

    device.vm.provider "virtualbox" do |v|
      v.name = "routerA"
      v.memory = 768
    end
    #   see note here: https://github.com/pradels/vagrant-libvirt#synced-folders
    device.vm.synced_folder ".", "/vagrant", disabled: true

    # NETWORK INTERFACES
      device.vm.network "private_network", ip: "192.168.0.100"

      # link for eth --> routerA <-> routerB
      device.vm.network "private_network", virtualbox__intnet: "net5", auto_config: false

  end

  ##### DEFINE VM for right_router #####
  config.vm.define "routerB" do |device|

    device.vm.hostname = "routerB"
    device.vm.box = "higebu/vyos"
    device.vm.box_version = "1.1.7"

    device.vm.provider "virtualbox" do |v|
      v.name = "routerB"
      v.memory = 768
    end
    #   see note here: https://github.com/pradels/vagrant-libvirt#synced-folders
    device.vm.synced_folder ".", "/vagrant", disabled: true

    # NETWORK INTERFACES
      device.vm.network "private_network", ip: "192.168.0.101"

      # link for eth --> routerB <-> routerA
      device.vm.network "private_network", virtualbox__intnet: "net5", auto_config: false

  end

  ##### DEFINE VM for MGMT #####
  config.vm.define "mgmt" do |device|
    device.vm.hostname = "mgmt"

    device.vm.box = "ubuntu/bionic64"
    device.vm.provider "virtualbox" do |v|
      v.name = "mgmt"
      v.linked_clone = true
      v.memory = 512
    end
    #   see note here: https://github.com/pradels/vagrant-libvirt#synced-folders
    device.vm.synced_folder ".", "/vagrant"

    device.vm.network "private_network", ip: "192.168.0.200"

    # Fixes "stdin: is not a tty" and "mesg: ttyname failed : Inappropriate ioctl for device"  messages --> https://github.com/mitchellh/vagrant/issues/1673
    device.vm.provision :shell , inline: "(sudo grep -q 'mesg n' /root/.profile 2>/dev/null && sudo sed -i '/mesg n/d' /root/.profile  2>/dev/null) || true;", privileged: false

    # Shorten Boot Process - Applies to Ubuntu Only - remove \"Wait for Network\"
    device.vm.provision :shell , inline: "sed -i 's/sleep [0-9]*/sleep 1/' /etc/init/failsafe.conf 2>/dev/null || true"

    # Copy hosts file to /etc/hosts
    device.vm.provision :shell , inline: "sudo cp /vagrant/vagrant/hosts /etc/hosts"

    # Copy secret key
    device.vm.provision :shell , inline: "sudo cp /vagrant/vagrant/id_rsa /home/vagrant/.ssh/id_rsa"

    # Install Ansible
    device.vm.provision :shell , path: "./vagrant/install_ansible.sh"

    # Install pip3
    device.vm.provision :shell , inline: "sudo apt -y install python3-pip"

  end

end
