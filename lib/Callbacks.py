from stable_baselines3.common.callbacks import BaseCallback
# from tqdm.auto import tqdm


class TensorboardCallback(BaseCallback):
    """
    Custom callback for plotting additional values in tensorboard.
    """

    def __init__(self, verbose=0):
        super().__init__(verbose)

    def _on_step(self) -> bool:

        self.logger.record("step_reward", self.locals['rewards'][0])

        return True


class ProgressBarCallback(BaseCallback):
    """
    :param pbar: (tqdm.pbar) Progress bar object
    """

    def __init__(self, pbar):
        super().__init__()
        self._pbar = pbar

    def _on_step(self):
        # Update the progress bar:
        self._pbar.n = self.num_timesteps
        self._pbar.update(0)

# this callback uses the 'with' block, allowing for correct initialisation and destruction


# class ProgressBarManager(object):
#     def __init__(self, total_timesteps):  # init object with total timesteps
#         self.pbar = None
#         self.total_timesteps = total_timesteps

#     def __enter__(self):  # create the progress bar and callback, return the callback
#         self.pbar = tqdm(total=self.total_timesteps)

#         return ProgressBarCallback(self.pbar)

#     def __exit__(self, exc_type, exc_val, exc_tb):  # close the callback
#         self.pbar.n = self.total_timesteps
#         self.pbar.update(0)
#         self.pbar.close()
