"""Default implementations."""

from protocol_tests.backchannel import (
    Backchannel, SubjectConnectionInfo
)
from protocol_tests.connection.backchannel import ConnectionsBackchannel


def pause():
    """Pause for input before continuing."""
    input('Press ENTER to continue.')


class ManualBackchannel(Backchannel, ConnectionsBackchannel):
    """
    Manually complete backchannel actions by copying and pasting values between
    subject and terminal.
    """
    async def setup(self, config, suite):
        pass

    async def reset(self):
        print('Reset test subject to clean state.')
        pause()

    async def new_connection(self, info, parameters=None):
        print(
            'Enter the following info into your agent '
            'to create a new connection:\n'
        )
        print('DID: {}\nVerkey: {}\nLabel: {}\nEndpoint: {}\n'.format(
            info.did, info.verkey, info.label, info.endpoint
        ))
        did = input('Input connection DID generated by test subject: ')
        recipients = input(
            'Input recipients as comma-separated, base58-encoded values: '
        )
        recipients = map(lambda recip: recip.strip(), recipients.split(','))
        recipients = list(filter(lambda recip: recip, recipients))
        routing_keys = input(
            'Input routing keys as comma-separated, base58-encoded values'
            ' (hit ENTER for none): '
        )
        routing_keys = map(
            lambda recip: recip.strip(), routing_keys.split(',')
        )
        routing_keys = list(filter(lambda recip: recip, routing_keys))
        endpoint = input('Input connection endpoint: ')

        return SubjectConnectionInfo(did, recipients, routing_keys, endpoint)

    async def connections_v1_0_inviter_start(self) -> str:
        print('Generate a new invitation on test subject.')
        return input('Enter invitation URL: ')

    async def connections_v1_0_invitee_start(self, invite):
        print('Paste the following invitation into the test subject.')
        print('Generated invitation: ', invite)
        pause()
