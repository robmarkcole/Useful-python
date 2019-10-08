import streamlit.ReportThread as ReportThread
from streamlit.server.Server import Server


class ThreadSafeSt():
    def __init__(self):
        """Object that write to a Streamlit app outside the main thread.
        
        This object must be created from the main thread, and then passed
        around to other threads so they can write to the Streamlit app.

        Example
        -------

        >>> # This must be called from the main thread:
        >>> thread_safe_st = ThreadSafeSt()
        >>>
        >>> def function_called_from_another_thread(arg1, arg2, st):
        ...   st.main.markdown('arg1 is: %s' % arg1)
        ...   st.sidebar.markdown('arg2 is: %s' % arg2)
        >>>
        >>> # On another thread:
        >>> function_called_from_another_thread(10, 20, thread_safe_st)

        """
        ctx = ReportThread.get_report_ctx()
        self.main = ctx.main_dg
        self.sidebar = ctx.sidebar_dg