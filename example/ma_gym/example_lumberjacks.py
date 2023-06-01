from environment.ma_gym.multi_agent_gym_environment import MultiAgentGymEnvironment
from solver.ma_gym.multi_agent_gym_solver import MultiAgentGymSolver
from utils.training_evaluation_pipeline import experimental_training_evaluation_pipeline

environment = MultiAgentGymEnvironment(env_to_load='ma_gym:Lumberjacks-v0')
experimental_training_evaluation_pipeline(environment, MultiAgentGymSolver)
