from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.increments('id')
            table.string('username')
            table.string('password')
            table.string('rol')
            table.string('name')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
