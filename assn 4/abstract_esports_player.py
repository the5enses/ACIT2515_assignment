class AbstractEsportsPlayer:
    """ Maintains details of an EsportsPlayer """

    def __init__(self, id, first_name, last_name, player_name, age, type):
        """ Initializes the attributes of an EsportsPlayer """
        AbstractEsportsPlayer._validate_input_integer('ID', id)
        self._id = id

        AbstractEsportsPlayer._validate_input_string('First Name', first_name)
        self._first_name = first_name

        AbstractEsportsPlayer._validate_input_string('Last Name', last_name)
        self._last_name = last_name

        AbstractEsportsPlayer._validate_input_string('Player Name', player_name)
        self._player_name = player_name

        AbstractEsportsPlayer._validate_input_integer('Age', age)
        self._age = age

        AbstractEsportsPlayer._validate_input_string('Type', type)
        self._type = type

    def get_first_name(self):
        """ Returns player's first name """
        return self._first_name

    def get_last_name(self):
        """ Returns player's last name """
        return self._last_name

    def get_full_name(self):
        """ Returns the player's full name """
        return "%s %s" % (self._first_name, self._last_name)

    def get_player_name(self):
        """ Returns the player's in-game name """
        return self._player_name

    def get_age(self):
        """ Returns the player's age """
        return self._age

    def get_details(self):
        """ Returns details """
        raise NotImplementedError("Must implement in subclasses")

    def get_type(self):
        """ Returns type """
        raise NotImplementedError("Must implement in subclasses")

    def to_dict(self):
        raise NotImplementedError("must implement in subclass")

    @staticmethod
    def _validate_input_string(display_name, value):
        """Private helper to validate values"""

        if value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if value == "":
            raise ValueError(display_name + " cannot be empty.")

    @staticmethod
    def _validate_input_integer(display_name, value):
        """Private helper to validate values"""

        if isinstance(value, int) is False:
            raise ValueError(display_name + " must be integer.")
