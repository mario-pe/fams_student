resource "aws_vpc" "gstudent-vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = {
    Name = "gstudent"
  }
}

resource "aws_subnet" "gstudent-subnet-prv-1" {
  vpc_id = aws_vpc.gstudent-vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "eu-west-1a"
  tags = {
    Name = "gstudent"
  }
}

resource "aws_subnet" "gstudent-subnet-prv-2" {
  vpc_id     = aws_vpc.gstudent-vpc.id
  cidr_block = "10.0.3.0/24"
  availability_zone = "eu-west-1b"

  tags = {
    Name = "gstudent"
  }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.gstudent-vpc.id
  tags = {
    Name = "gstudent"
  }
}

resource "aws_route_table" "rt" {
  vpc_id = aws_vpc.gstudent-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }


  tags = {
    Name = "gstudent"
  }
}

resource "aws_subnet" "gstudent-subnet-public" {
  vpc_id     = aws_vpc.gstudent-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-west-1a"

  tags = {
    Name = "gstudent"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.gstudent-subnet-public.id
  route_table_id = aws_route_table.rt.id
}

resource "aws_network_interface" "gstudent_ni" {
  subnet_id       = aws_subnet.gstudent-subnet-public.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.sg.id]

  tags = {
    Name = "gstudent"
  }
}

resource "aws_security_group" "sg" {
  vpc_id      = aws_vpc.gstudent-vpc.id
  name        = "allow_web_traffic"
  description = "Allow web traffic"

   ingress {
     description = "APP"
     from_port   = 5000
     to_port     = 5000
     protocol    = "tcp"
     cidr_blocks = ["89.161.50.179/32"]
   }
   ingress {
     description = "Postgres"
     from_port   = 5432
     to_port     = 5432
     protocol    = "tcp"
     cidr_blocks = ["10.0.2.0/24", "10.0.3.0/24"]
   }
   egress {
     from_port   = 0
     to_port     = 0
     protocol    = "-1"
     cidr_blocks = ["0.0.0.0/0"]
   }

  tags = {
    Name = "gstudent"
  }
}

resource "aws_security_group" "rds-sg" {
  name   = "gstudent_rds_sg"
  vpc_id = aws_vpc.gstudent-vpc.id

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "gstudent_rds"
  }
}

resource "aws_eip" "geip" {
  vpc      = true
  network_interface = aws_network_interface.gstudent_ni.id
  associate_with_private_ip = "10.0.1.50"
  tags = {
    Name = "gstudent"
  }
}

//resource "aws_instance" "ws" {
//  ami           = "ami-0a8e758f5e873d1c1"
//  instance_type = "t3.micro"
//  availability_zone = "eu-west-1a"
//  key_name = "gstudent"
//
//  network_interface {
//    device_index = 0
//    network_interface_id = aws_network_interface.gstudent_ni.id
//  }
//
//  user_data = <<-EOF
//              #!/bin/bash
//              sudo apt update -y
//              sudo apt install apache2 -y
//              sudo systemctl start apache2
//              sudo bash -c 'echo hello world > /var/www/html/index.html'
//              EOF
//  tags = {
//    Name = "gstudent"
//  }
//}






