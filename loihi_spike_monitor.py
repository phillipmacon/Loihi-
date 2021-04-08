from brian2 import SpikeMonitor

class LoihiSpikeMonitor(SpikeMonitor):
    """
    The LoihiSpikeMonitor extends the SpikeMonitor class from Brian2.

    This class creates a Brian2 spike monitor and updates the schedule for
    reading the monitored values. This schedule change is performed to
    produce the same outputs as in Loihi.

    Methods
    -------
    __init__(source, variable, record=True, order=0)
        Initializes the LoihiSpikeMonitor and the SpikeMonitor
    """

    def __init__(self, source, variable=None, order=None):
        """ Initializes the LoihiSpikeMonitor and the SpikeMonitor

        First, a SpikeMonitor is initialized, based on the given parameters.
        Afterwards, the schedule for monitoring the values is updated.
        Parameters
        ----------
        source : `Group`
            Which object to record values from.
        variable : str
            Which variable to record, check the `state` object for details.
        order : int, optional
            The priority of of this group for operations occurring at the same time
            step and in the same scheduling slot. Defaults to 0.
        """

        # Define Brian spike monitor
        super().__init__(
            source,
            variable,
            order=order
        )

        # Update when states should be monitored
        self.when = 'end'