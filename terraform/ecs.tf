resource "aws_ecs_cluster" "gstudnet-terra-cluster" {
  name = "gstudent"
}

resource "aws_cloudwatch_log_group" "gstudent_logs" {
  name = "gstudent_logs"
  retention_in_days = 1
  tags = {
    Name = "gstudent"
  }
}
resource "aws_cloudwatch_log_stream" "gstudent_log_stream" {
  name           = "gstudent-log-stream"
  log_group_name = aws_cloudwatch_log_group.gstudent_logs.name
}


resource "aws_ecs_service" "gstudent_service" {
  name = "gstudent_service"
  cluster = aws_ecs_cluster.gstudnet-terra-cluster.id
  task_definition = aws_ecs_task_definition.gstudent_tasks.arn
  desired_count = 1
  launch_type = "FARGATE"
  network_configuration {
    subnets = [aws_subnet.gstudent-subnet-public.id]
    security_groups = [aws_security_group.sg.id]
    assign_public_ip = true
  }
  depends_on = [aws_iam_role_policy_attachment.ecs_task_execution_role]
  tags = {
    Name = "gstudent"
  }
}


resource "aws_ecs_task_definition" "gstudent_tasks" {
  family = "gstudent_tasks_terraform"
  container_definitions = jsonencode([
    {
      name      = "gstudent_task"
      image     = "public.ecr.aws/z8r2b2t5/gstudent:latest"
      cpu       = 1024
      memory    = 2048
      network_mode = "awsvpc" // test
      portMappings = [
        {
          containerPort = 5000
          hostPort      = 5000
        }
      ]
      logConfiguration: {
          logDriver: "awslogs"
          options: {
            awslogs-group: "gstudent_logs"
            awslogs-region: "eu-west-1"
            awslogs-stream-prefix: "gstudent-log-stream"
          }
        }
    }
  ])
  cpu = 1024
  memory = 2048
  network_mode = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn
}
