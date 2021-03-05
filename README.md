# supreme_cop_bot
Python script using a SupremeBot class and various methods that takes various parts of information in order to automate the ordering process

Information taken includes
- Product info (Size, colour, name, etc)
- Payment info (Card details, etc)
- Address info (House number, postcode)
- Personal info (Email, name, number)

This bot is designed only for use with the supreme new york website. It will not work with other sites as the name values in the HTML will likely differ.
It would be fairly straight forward to adapt this for another site, you would merely need to replace the find_by_x statements with the correct HTML names for
the different forms.

Supreme has allegedly been banning IPs who use bots, so use at your own risk.

Also note, you will need GeckDriver if you intend to use Firefox (like I did), or some other driver for a different browser. If you're doing this yourself, you
will need to add that driver to the path in your machine.
