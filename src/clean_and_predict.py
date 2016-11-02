import cPickle as pickle


class DataCleaner(object):
    def __init__(self, cleaning_script=None):
        self.cleaning_script = cleaning_script

    def load_cleaning_script(self, cleaning_script):
        """
        Loads a new cleaning script into the class. The cleaning script must
        be a module that has a function .clean() that takes a JSON object as
        input.

        Parameters
        ----------
        cleaning_script: module
            Module containing the cleaning script

        Returns
        -------
        None
        """
        pass

    def clean_data(self, raw_json):
        """
        Returns the clean JSON data after cleaning the raw JSON according
        to the scheme used during training and loaded into this class.

        Parameters
        ----------
        raw_json: JSON str
            JSON object of raw data sent by POST request

        Returns
        -------
        clean_json: JSON str
            Cleaned JSON object of raw data sent by POST request
        """
        pass


class MyModel(object):
    def __init__(self, model=None):
        self.model = model

    def load_model(self, filename):
        """
        Loads a new model into the class. The model must be stored in a pickle
        file.

        Parameters
        ----------
        filename: str
            The filename of a pickle file containing the modelmodule

        Returns
        -------
        None
        """
        with open(filename) as f:
            model = pickle.load(f)
            self.model = model

    def transform(self, clean_data):
        """
        Returns a numpy array of data for the model to predict.

        Prepares the cleaned JSON by converting it to a data type that the
        model can use to predict.

        Parameters
        ----------
        clean_data: JSON str
            JSON object of clean data sent by POST request

        Returns
        -------
        prepped_data: numpy array
            Cleaned data to be used in prediction
        """
        pass

    def predict(self, prepped_data):
        """
        Returns a probability the event is fraud and a risk label for
        the prepped_data.

        Parameters
        ----------
        prepped_data: numpy array
            Array object of clean data sent by POST request

        Returns
        -------
        fraud_proba: float
            Cleaned data to be used in prediction
        risk_label: str
            Risk level based on thresholds
        """
        pass

    def transform_predict(self, clean_data):
        """
        Returns a probability the event is fraud and a risk label for
        the clean JSON data input.

        Converts the cleaned JSON to a numpy array and then uses the loaded
        model to do a prediction.

        Parameters
        ----------
        clean_data: JSON str
            JSON object of clean data sent by POST request

        Returns
        -------
        fraud_proba: float
            Cleaned data to be used in prediction
        risk_label: str
            Risk level based on thresholds
        """
        pass
