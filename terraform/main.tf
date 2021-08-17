resource "aws_db_subnet_group" "db-subnet-group" {
  name       = "db-subnet"
  subnet_ids = [aws_subnet.gstudent-subnet-prv-1.id, aws_subnet.gstudent-subnet-prv-2.id]
  tags = {
    Name = "gstudent"
  }
}

resource "aws_db_instance" "gstudent_db" {
  identifier             = "gstudent"
  instance_class         = "db.t3.micro"
  allocated_storage      = 5
  engine                 = "postgres"
  engine_version         = "13.1"
  username               = "postgres"
  password               = "postgres"
  name                   = "student"
  db_subnet_group_name   = aws_db_subnet_group.db-subnet-group.name
  vpc_security_group_ids = [aws_security_group.rds-sg.id]
  parameter_group_name   = aws_db_parameter_group.gstudent_params.name
  publicly_accessible    = true
  skip_final_snapshot    = true
  tags = {
    Name = "gstudent"
  }
}

resource "aws_db_parameter_group" "gstudent_params" {
  name   = "student"
  family = "postgres13"

  parameter {
    name  = "log_connections"
    value = "1"
  }
}
