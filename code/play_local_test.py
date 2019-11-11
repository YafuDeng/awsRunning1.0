from dlgo.gtp.play_local import LocalGtpBot
from dlgo.agent.termination import PassWhenOpponentPasses
from dlgo.agent.predict import load_prediction_agent
import h5py

bot = load_prediction_agent(h5py.File("agents/betago.hdf5", "r"))

gpt_bot = LocalGtpBot(go_bot = bot, termination = PassWhenOpponentPasses(),
				handicap=0, opponent='pachi')

gpt_bot.run()
