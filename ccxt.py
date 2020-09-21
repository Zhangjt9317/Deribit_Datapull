

from ccxt.async_support.base.exchange import Exchange
import hashlib
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import ArgumentsRequired
from ccxt.base.errors import BadRequest
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidAddress
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import NotSupported
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import OnMaintenance
from ccxt.base.decimal_to_precision import TICK_SIZE


class deribit(Exchange):

    def describe(self):
        return self.deep_extend(super(deribit, self).describe(), {
            'id': 'deribit',
            'name': 'Deribit',
            'countries': ['NL'],  # Netherlands
            'version': 'v2',
            'userAgent': None,
            'rateLimit': 500,
            'has': {
                'cancelAllOrders': True,
                'cancelOrder': True,
                'CORS': True,
                'createDepositAddress': True,
                'createOrder': True,
                'editOrder': True,
                'fetchBalance': True,
                'fetchClosedOrders': True,
                'fetchDepositAddress': True,
                'fetchDeposits': True,
                'fetchMarkets': True,
                'fetchMyTrades': True,
                'fetchOHLCV': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrders': False,
                'fetchOrderTrades': True,
                'fetchStatus': True,
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchTime': True,
                'fetchTrades': True,
                'fetchTransactions': False,
                'fetchWithdrawals': True,
                'withdraw': True,
            },
            'timeframes': {
                '1m': '1',
                '3m': '3',
                '5m': '5',
                '10m': '10',
                '15m': '15',
                '30m': '30',
                '1h': '60',
                '2h': '120',
                '3h': '180',
                '6h': '360',
                '12h': '720',
                '1d': '1D',
            },
            'urls': {
                'test': 'https://test.deribit.com',
                'logo': 'https://user-images.githubusercontent.com/1294454/41933112-9e2dd65a-798b-11e8-8440-5bab2959fcb8.jpg',
                'api': 'https://www.deribit.com',
                'www': 'https://www.deribit.com',
                'doc': [
                    'https://docs.deribit.com/v2',
                    'https://github.com/deribit',
                ],
                'fees': 'https://www.deribit.com/pages/information/fees',
                'referral': 'https://www.deribit.com/reg-1189.4038',
            },
            'api': {
                'public': {
                    'get': [
                        # Authentication
                        'auth',
                        'exchange_token',
                        'fork_token',
                        # Session management
                        'set_heartbeat',
                        'disable_heartbeat',
                        # Supporting
                        'get_time',
                        'hello',
                        'test',
                        # Subscription management
                        'subscribe',
                        'unsubscribe',
                        # Account management
                        'get_announcements',
                        # Market data
                        'get_book_summary_by_currency',
                        'get_book_summary_by_instrument',
                        'get_contract_size',
                        'get_currencies',
                        'get_funding_chart_data',
                        'get_funding_rate_history',
                        'get_funding_rate_value',
                        'get_historical_volatility',
                        'get_index',
                        'get_instruments',
                        'get_last_settlements_by_currency',
                        'get_last_settlements_by_instrument',
                        'get_last_trades_by_currency',
                        'get_last_trades_by_currency_and_time',
                        'get_last_trades_by_instrument',
                        'get_last_trades_by_instrument_and_time',
                        'get_order_book',
                        'get_trade_volumes',
                        'get_tradingview_chart_data',
                        'ticker',
                    ],
                },
                'private': {
                    'get': [
                        # Authentication
                        'logout',
                        # Session management
                        'enable_cancel_on_disconnect',
                        'disable_cancel_on_disconnect',
                        'get_cancel_on_disconnect',
                        # Subscription management
                        'subscribe',
                        'unsubscribe',
                        # Account management
                        'change_api_key_name',
                        'change_scope_in_api_key',
                        'change_subaccount_name',
                        'create_api_key',
                        'create_subaccount',
                        'disable_api_key',
                        'disable_tfa_for_subaccount',
                        'enable_api_key',
                        'get_account_summary',
                        'get_email_language',
                        'get_new_announcements',
                        'get_position',
                        'get_positions',
                        'get_subaccounts',
                        'list_api_keys',
                        'remove_api_key',
                        'reset_api_key',
                        'set_announcement_as_read',
                        'set_api_key_as_default',
                        'set_email_for_subaccount',
                        'set_email_language',
                        'set_password_for_subaccount',
                        'toggle_notifications_from_subaccount',
                        'toggle_subaccount_login',
                        # Block Trade
                        'execute_block_trade',
                        'get_block_trade',
                        'get_last_block_trades_by_currency',
                        'invalidate_block_trade_signature',
                        'verify_block_trade',
                        # Trading
                        'buy',
                        'sell',
                        'edit',
                        'cancel',
                        'cancel_all',
                        'cancel_all_by_currency',
                        'cancel_all_by_instrument',
                        'cancel_by_label',
                        'close_position',
                        'get_margins',
                        'get_open_orders_by_currency',
                        'get_open_orders_by_instrument',
                        'get_order_history_by_currency',
                        'get_order_history_by_instrument',
                        'get_order_margin_by_ids',
                        'get_order_state',
                        'get_stop_order_history',
                        'get_user_trades_by_currency',
                        'get_user_trades_by_currency_and_time',
                        'get_user_trades_by_instrument',
                        'get_user_trades_by_instrument_and_time',
                        'get_user_trades_by_order',
                        'get_settlement_history_by_instrument',
                        'get_settlement_history_by_currency',
                        # Wallet
                        'cancel_transfer_by_id',
                        'cancel_withdrawal',
                        'create_deposit_address',
                        'get_current_deposit_address',
                        'get_deposits',
                        'get_transfers',
                        'get_withdrawals',
                        'submit_transfer_to_subaccount',
                        'submit_transfer_to_user',
                        'withdraw',
                    ],
                },
            },
            'exceptions': {
                # 0 or absent Success, No error.
                '9999': PermissionDenied,  # 'api_not_enabled' User didn't enable API for the Account.
                '10000': AuthenticationError,
                # 'authorization_required' Authorization issue, invalid or absent signature etc.
                '10001': ExchangeError,  # 'error' Some general failure, no public information available.
                '10002': InvalidOrder,  # 'qty_too_low' Order quantity is too low.
                '10003': InvalidOrder,
                # 'order_overlap' Rejection, order overlap is found and self-trading is not enabled.
                '10004': OrderNotFound,
                # 'order_not_found' Attempt to operate with order that can't be found by specified id.
                '10005': InvalidOrder,
                # 'price_too_low <Limit>' Price is too low, <Limit> defines current limit for the operation.
                '10006': InvalidOrder,
                # 'price_too_low4idx <Limit>' Price is too low for current index, <Limit> defines current bottom limit for the operation.
                '10007': InvalidOrder,
                # 'price_too_high <Limit>' Price is too high, <Limit> defines current up limit for the operation.
                '10008': InvalidOrder,
                # 'price_too_high4idx <Limit>' Price is too high for current index, <Limit> defines current up limit for the operation.
                '10009': InsufficientFunds,  # 'not_enough_funds' Account has not enough funds for the operation.
                '10010': OrderNotFound,  # 'already_closed' Attempt of doing something with closed order.
                '10011': InvalidOrder,  # 'price_not_allowed' This price is not allowed for some reason.
                '10012': InvalidOrder,  # 'book_closed' Operation for instrument which order book had been closed.
                '10013': PermissionDenied,
                # 'pme_max_total_open_orders <Limit>' Total limit of open orders has been exceeded, it is applicable for PME users.
                '10014': PermissionDenied,
                # 'pme_max_future_open_orders <Limit>' Limit of count of futures' open orders has been exceeded, it is applicable for PME users.
                '10015': PermissionDenied,
                # 'pme_max_option_open_orders <Limit>' Limit of count of options' open orders has been exceeded, it is applicable for PME users.
                '10016': PermissionDenied,
                # 'pme_max_future_open_orders_size <Limit>' Limit of size for futures has been exceeded, it is applicable for PME users.
                '10017': PermissionDenied,
                # 'pme_max_option_open_orders_size <Limit>' Limit of size for options has been exceeded, it is applicable for PME users.
                '10018': PermissionDenied,
                # 'non_pme_max_future_position_size <Limit>' Limit of size for futures has been exceeded, it is applicable for non-PME users.
                '10019': PermissionDenied,  # 'locked_by_admin' Trading is temporary locked by admin.
                '10020': ExchangeError,  # 'invalid_or_unsupported_instrument' Instrument name is not valid.
                '10021': InvalidOrder,  # 'invalid_amount' Amount is not valid.
                '10022': InvalidOrder,  # 'invalid_quantity' quantity was not recognized as a valid number(for API v1).
                '10023': InvalidOrder,  # 'invalid_price' price was not recognized as a valid number.
                '10024': InvalidOrder,  # 'invalid_max_show' max_show parameter was not recognized as a valid number.
                '10025': InvalidOrder,
                # 'invalid_order_id' Order id is missing or its format was not recognized as valid.
                '10026': InvalidOrder,  # 'price_precision_exceeded' Extra precision of the price is not supported.
                '10027': InvalidOrder,
                # 'non_integer_contract_amount' Futures contract amount was not recognized as integer.
                '10028': DDoSProtection,  # 'too_many_requests' Allowed request rate has been exceeded.
                '10029': OrderNotFound,  # 'not_owner_of_order' Attempt to operate with not own order.
                '10030': ExchangeError,  # 'must_be_websocket_request' REST request where Websocket is expected.
                '10031': ExchangeError,  # 'invalid_args_for_instrument' Some of arguments are not recognized as valid.
                '10032': InvalidOrder,  # 'whole_cost_too_low' Total cost is too low.
                '10033': NotSupported,  # 'not_implemented' Method is not implemented yet.
                '10034': InvalidOrder,  # 'stop_price_too_high' Stop price is too high.
                '10035': InvalidOrder,  # 'stop_price_too_low' Stop price is too low.
                '10036': InvalidOrder,  # 'invalid_max_show_amount' Max Show Amount is not valid.
                '10040': ExchangeNotAvailable,  # 'retry' Request can't be processed right now and should be retried.
                '10041': OnMaintenance,
                # 'settlement_in_progress' Settlement is in progress. Every day at settlement time for several seconds, the system calculates user profits and updates balances. That time trading is paused for several seconds till the calculation is completed.
                '10043': InvalidOrder,  # 'price_wrong_tick' Price has to be rounded to a certain tick size.
                '10044': InvalidOrder,  # 'stop_price_wrong_tick' Stop Price has to be rounded to a certain tick size.
                '10045': InvalidOrder,  # 'can_not_cancel_liquidation_order' Liquidation order can't be canceled.
                '10046': InvalidOrder,  # 'can_not_edit_liquidation_order' Liquidation order can't be edited.
                '10047': DDoSProtection,
                # 'matching_engine_queue_full' Reached limit of pending Matching Engine requests for user.
                '10048': ExchangeError,  # 'not_on_self_server' The requested operation is not available on self server.
                '11008': InvalidOrder,  # 'already_filled' This request is not allowed in regards to the filled order.
                '11029': BadRequest,  # 'invalid_arguments' Some invalid input has been detected.
                '11030': ExchangeError,
                # 'other_reject <Reason>' Some rejects which are not considered as very often, more info may be specified in <Reason>.
                '11031': ExchangeError,
                # 'other_error <Error>' Some errors which are not considered as very often, more info may be specified in <Error>.
                '11035': DDoSProtection,  # 'no_more_stops <Limit>' Allowed amount of stop orders has been exceeded.
                '11036': InvalidOrder,
                # 'invalid_stoppx_for_index_or_last' Invalid StopPx(too high or too low) as to current index or market.
                '11037': BadRequest,  # 'outdated_instrument_for_IV_order' Instrument already not available for trading.
                '11038': InvalidOrder,  # 'no_adv_for_futures' Advanced orders are not available for futures.
                '11039': InvalidOrder,  # 'no_adv_postonly' Advanced post-only orders are not supported yet.
                '11041': InvalidOrder,
                # 'not_adv_order' Advanced order properties can't be set if the order is not advanced.
                '11042': PermissionDenied,  # 'permission_denied' Permission for the operation has been denied.
                '11043': BadRequest,  # 'bad_argument' Bad argument has been passed.
                '11044': InvalidOrder,  # 'not_open_order' Attempt to do open order operations with the not open order.
                '11045': BadRequest,  # 'invalid_event' Event name has not been recognized.
                '11046': BadRequest,
                # 'outdated_instrument' At several minutes to instrument expiration, corresponding advanced implied volatility orders are not allowed.
                '11047': BadRequest,
                # 'unsupported_arg_combination' The specified combination of arguments is not supported.
                '11048': ExchangeError,  # 'wrong_max_show_for_option' Wrong Max Show for options.
                '11049': BadRequest,  # 'bad_arguments' Several bad arguments have been passed.
                '11050': BadRequest,  # 'bad_request' Request has not been parsed properly.
                '11051': OnMaintenance,  # 'system_maintenance' System is under maintenance.
                '11052': ExchangeError,
                # 'subscribe_error_unsubscribed' Subscription error. However, subscription may fail without self error, please check list of subscribed channels returned, as some channels can be not subscribed due to wrong input or lack of permissions.
                '11053': ExchangeError,  # 'transfer_not_found' Specified transfer is not found.
                '11090': InvalidAddress,  # 'invalid_addr' Invalid address.
                '11091': InvalidAddress,  # 'invalid_transfer_address' Invalid addres for the transfer.
                '11092': InvalidAddress,  # 'address_already_exist' The address already exists.
                '11093': DDoSProtection,  # 'max_addr_count_exceeded' Limit of allowed addresses has been reached.
                '11094': ExchangeError,
                # 'internal_server_error' Some unhandled error on server. Please report to admin. The details of the request will help to locate the problem.
                '11095': ExchangeError,
                # 'disabled_deposit_address_creation' Deposit address creation has been disabled by admin.
                '11096': ExchangeError,  # 'address_belongs_to_user' Withdrawal instead of transfer.
                '12000': AuthenticationError,  # 'bad_tfa' Wrong TFA code
                '12001': DDoSProtection,  # 'too_many_subaccounts' Limit of subbacounts is reached.
                '12002': ExchangeError,  # 'wrong_subaccount_name' The input is not allowed as name of subaccount.
                '12998': AuthenticationError,  # 'tfa_over_limit' The number of failed TFA attempts is limited.
                '12003': AuthenticationError,  # 'login_over_limit' The number of failed login attempts is limited.
                '12004': AuthenticationError,
                # 'registration_over_limit' The number of registration requests is limited.
                '12005': AuthenticationError,  # 'country_is_banned' The country is banned(possibly via IP check).
                '12100': ExchangeError,
                # 'transfer_not_allowed' Transfer is not allowed. Possible wrong direction or other mistake.
                '12999': AuthenticationError,
                # 'tfa_used' TFA code is correct but it is already used. Please, use next code.
                '13000': AuthenticationError,
                # 'invalid_login' Login name is invalid(not allowed or it contains wrong characters).
                '13001': AuthenticationError,  # 'account_not_activated' Account must be activated.
                '13002': PermissionDenied,  # 'account_blocked' Account is blocked by admin.
                '13003': AuthenticationError,  # 'tfa_required' This action requires TFA authentication.
                '13004': AuthenticationError,  # 'invalid_credentials' Invalid credentials has been used.
                '13005': AuthenticationError,  # 'pwd_match_error' Password confirmation error.
                '13006': AuthenticationError,  # 'security_error' Invalid Security Code.
                '13007': AuthenticationError,  # 'user_not_found' User's security code has been changed or wrong.
                '13008': ExchangeError,  # 'request_failed' Request failed because of invalid input or internal failure.
                '13009': AuthenticationError,
                # 'unauthorized' Wrong or expired authorization token or bad signature. For example, please check scope of the token, 'connection' scope can't be reused for other connections.
                '13010': BadRequest,  # 'value_required' Invalid input, missing value.
                '13011': BadRequest,  # 'value_too_short' Input is too short.
                '13012': PermissionDenied,  # 'unavailable_in_subaccount' Subaccount restrictions.
                '13013': BadRequest,  # 'invalid_phone_number' Unsupported or invalid phone number.
                '13014': BadRequest,  # 'cannot_send_sms' SMS sending failed -- phone number is wrong.
                '13015': BadRequest,  # 'invalid_sms_code' Invalid SMS code.
                '13016': BadRequest,  # 'invalid_input' Invalid input.
                '13017': ExchangeError,  # 'subscription_failed' Subscription hailed, invalid subscription parameters.
                '13018': ExchangeError,  # 'invalid_content_type' Invalid content type of the request.
                '13019': ExchangeError,  # 'orderbook_closed' Closed, expired order book.
                '13020': ExchangeError,  # 'not_found' Instrument is not found, invalid instrument name.
                '13021': PermissionDenied,  # 'forbidden' Not enough permissions to execute the request, forbidden.
                '13025': ExchangeError,
                # 'method_switched_off_by_admin' API method temporarily switched off by administrator.
                '-32602': BadRequest,  # 'Invalid params' see JSON-RPC spec.
                '-32601': BadRequest,  # 'Method not found' see JSON-RPC spec.
                '-32700': BadRequest,  # 'Parse error' see JSON-RPC spec.
                '-32000': BadRequest,  # 'Missing params' see JSON-RPC spec.
            },
            'precisionMode': TICK_SIZE,
            'options': {
                'code': 'BTC',
                'fetchBalance': {
                    'code': 'BTC',
                },
            },
        })

    async def fetch_time(self, params={}):
        response = await self.publicGetGetTime(params)
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: 1583922446019,
        #         usIn: 1583922446019955,
        #         usOut: 1583922446019956,
        #         usDiff: 1,
        #         testnet: False
        #     }
        #
        return self.safe_integer(response, 'result')

    def code_from_options(self, methodName):
        defaultCode = self.safe_value(self.options, 'code', 'BTC')
        options = self.safe_value(self.options, methodName, {})
        return self.safe_value(options, 'code', defaultCode)

    async def fetch_status(self, params={}):
        request = {
            # 'expected_result': False,  # True will trigger an error for testing purposes
        }
        await self.publicGetTest(self.extend(request, params))
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: {version: '1.2.26'},
        #         usIn: 1583922623964485,
        #         usOut: 1583922623964487,
        #         usDiff: 2,
        #         testnet: False
        #     }
        #
        self.status = self.extend(self.status, {
            'status': 'ok',
            'updated': self.milliseconds(),
        })
        return self.status

    async def fetch_markets(self, params={}):
        currenciesResponse = await self.publicGetGetCurrencies(params)
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: [
        #             {
        #                 withdrawal_priorities: [
        #                     {value: 0.15, name: 'very_low'},
        #                     {value: 1.5, name: 'very_high'},
        #                 ],
        #                 withdrawal_fee: 0.0005,
        #                 min_withdrawal_fee: 0.0005,
        #                 min_confirmations: 1,
        #                 fee_precision: 4,
        #                 currency_long: 'Bitcoin',
        #                 currency: 'BTC',
        #                 coin_type: 'BITCOIN'
        #             }
        #         ],
        #         usIn: 1583761588590479,
        #         usOut: 1583761588590544,
        #         usDiff: 65,
        #         testnet: False
        #     }
        #
        currenciesResult = self.safe_value(currenciesResponse, 'result', [])
        result = []
        for i in range(0, len(currenciesResult)):
            currencyId = self.safe_string(currenciesResult[i], 'currency')
            request = {
                'currency': currencyId,
            }
            instrumentsResponse = await self.publicGetGetInstruments(self.extend(request, params))
            #
            #     {
            #         jsonrpc: '2.0',
            #         result: [
            #             {
            #                 tick_size: 0.0005,
            #                 taker_commission: 0.0004,
            #                 strike: 300,
            #                 settlement_period: 'week',
            #                 quote_currency: 'USD',
            #                 option_type: 'call',
            #                 min_trade_amount: 1,
            #                 maker_commission: 0.0004,
            #                 kind: 'option',
            #                 is_active: True,
            #                 instrument_name: 'ETH-13MAR20-300-C',
            #                 expiration_timestamp: 1584086400000,
            #                 creation_timestamp: 1582790403000,
            #                 contract_size: 1,
            #                 base_currency: 'ETH'
            #             },
            #         ],
            #         usIn: 1583761889500586,
            #         usOut: 1583761889505066,
            #         usDiff: 4480,
            #         testnet: False
            #     }
            #
            instrumentsResult = self.safe_value(instrumentsResponse, 'result', [])
            for k in range(0, len(instrumentsResult)):
                market = instrumentsResult[k]
                id = self.safe_string(market, 'instrument_name')
                baseId = self.safe_string(market, 'base_currency')
                quoteId = self.safe_string(market, 'quote_currency')
                base = self.safe_currency_code(baseId)
                quote = self.safe_currency_code(quoteId)
                type = self.safe_string(market, 'kind')
                future = (type == 'future')
                option = (type == 'option')
                active = self.safe_value(market, 'is_active')
                minTradeAmount = self.safe_float(market, 'min_trade_amount')
                tickSize = self.safe_float(market, 'tick_size')
                precision = {
                    'amount': minTradeAmount,
                    'price': tickSize,
                }
                result.append({
                    'id': id,
                    'symbol': id,
                    'base': base,
                    'quote': quote,
                    'active': active,
                    'precision': precision,
                    'taker': self.safe_float(market, 'taker_commission'),
                    'maker': self.safe_float(market, 'maker_commission'),
                    'limits': {
                        'amount': {
                            'min': minTradeAmount,
                            'max': None,
                        },
                        'price': {
                            'min': tickSize,
                            'max': None,
                        },
                        'cost': {
                            'min': None,
                            'max': None,
                        },
                    },
                    'type': type,
                    'spot': False,
                    'future': future,
                    'option': option,
                    'info': market,
                })
        return result

    async def fetch_balance(self, params={}):
        await self.load_markets()
        code = self.code_from_options('fetchBalance')
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
        }
        response = await self.privateGetGetAccountSummary(self.extend(request, params))
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: {
        #             total_pl: 0,
        #             session_upl: 0,
        #             session_rpl: 0,
        #             session_funding: 0,
        #             portfolio_margining_enabled: False,
        #             options_vega: 0,
        #             options_theta: 0,
        #             options_session_upl: 0,
        #             options_session_rpl: 0,
        #             options_pl: 0,
        #             options_gamma: 0,
        #             options_delta: 0,
        #             margin_balance: 0.00062359,
        #             maintenance_margin: 0,
        #             limits: {
        #                 non_matching_engine_burst: 300,
        #                 non_matching_engine: 200,
        #                 matching_engine_burst: 20,
        #                 matching_engine: 2
        #             },
        #             initial_margin: 0,
        #             futures_session_upl: 0,
        #             futures_session_rpl: 0,
        #             futures_pl: 0,
        #             equity: 0.00062359,
        #             deposit_address: '13tUtNsJSZa1F5GeCmwBywVrymHpZispzw',
        #             delta_total: 0,
        #             currency: 'BTC',
        #             balance: 0.00062359,
        #             available_withdrawal_funds: 0.00062359,
        #             available_funds: 0.00062359
        #         },
        #         usIn: 1583775838115975,
        #         usOut: 1583775838116520,
        #         usDiff: 545,
        #         testnet: False
        #     }
        #
        result = {
            'info': response,
        }
        balance = self.safe_value(response, 'result', {})
        currencyId = self.safe_string(balance, 'currency')
        currencyCode = self.safe_currency_code(currencyId)
        account = self.account()
        account['free'] = self.safe_float(balance, 'availableFunds')
        account['used'] = self.safe_float(balance, 'maintenanceMargin')
        account['total'] = self.safe_float(balance, 'equity')
        result[currencyCode] = account
        return self.parse_balance(result)

    async def create_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
        }
        response = await self.privateGetCreateDepositAddress(self.extend(request, params))
        #
        #     {
        #         'jsonrpc': '2.0',
        #         'id': 7538,
        #         'result': {
        #             'address': '2N8udZGBc1hLRCFsU9kGwMPpmYUwMFTuCwB',
        #             'creation_timestamp': 1550575165170,
        #             'currency': 'BTC',
        #             'type': 'deposit'
        #         }
        #     }
        #
        result = self.safe_value(response, 'result', {})
        address = self.safe_string(result, 'address')
        self.check_address(address)
        return {
            'currency': code,
            'address': address,
            'tag': None,
            'info': response,
        }

    async def fetch_deposit_address(self, code, params={}):
        await self.load_markets()
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
        }
        response = await self.privateGetGetCurrentDepositAddress(self.extend(request, params))
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: {
        #             type: 'deposit',
        #             status: 'ready',
        #             requires_confirmation: True,
        #             currency: 'BTC',
        #             creation_timestamp: 1514694684651,
        #             address: '13tUtNsJSZa1F5GeCmwBywVrymHpZispzw'
        #         },
        #         usIn: 1583785137274288,
        #         usOut: 1583785137274454,
        #         usDiff: 166,
        #         testnet: False
        #     }
        #
        result = self.safe_value(response, 'result', {})
        address = self.safe_string(result, 'address')
        self.check_address(address)
        return {
            'currency': code,
            'address': address,
            'tag': None,
            'info': response,
        }

    def parse_ticker(self, ticker, market=None):
        #
        # fetchTicker /public/ticker
        #
        #     {
        #         timestamp: 1583778859480,
        #         stats: {volume: 60627.57263769, low: 7631.5, high: 8311.5},
        #         state: 'open',
        #         settlement_price: 7903.21,
        #         open_interest: 111543850,
        #         min_price: 7634,
        #         max_price: 7866.51,
        #         mark_price: 7750.02,
        #         last_price: 7750.5,
        #         instrument_name: 'BTC-PERPETUAL',
        #         index_price: 7748.01,
        #         funding_8h: 0.0000026,
        #         current_funding: 0,
        #         best_bid_price: 7750,
        #         best_bid_amount: 19470,
        #         best_ask_price: 7750.5,
        #         best_ask_amount: 343280
        #     }
        #
        # fetchTicker /public/get_book_summary_by_instrument
        # fetchTickers /public/get_book_summary_by_currency
        #
        #     {
        #         volume: 124.1,
        #         underlying_price: 7856.445926872601,
        #         underlying_index: 'SYN.BTC-10MAR20',
        #         quote_currency: 'USD',
        #         open_interest: 121.8,
        #         mid_price: 0.01975,
        #         mark_price: 0.01984559,
        #         low: 0.0095,
        #         last: 0.0205,
        #         interest_rate: 0,
        #         instrument_name: 'BTC-10MAR20-7750-C',
        #         high: 0.0295,
        #         estimated_delivery_price: 7856.29,
        #         creation_timestamp: 1583783678366,
        #         bid_price: 0.0185,
        #         base_currency: 'BTC',
        #         ask_price: 0.021
        #     },
        #
        timestamp = self.safe_integer_2(ticker, 'timestamp', 'creation_timestamp')
        marketId = self.safe_string(ticker, 'instrument_name')
        symbol = marketId
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
        if (symbol is None) and (market is not None):
            symbol = market['symbol']
        last = self.safe_float_2(ticker, 'last_price', 'last')
        stats = self.safe_value(ticker, 'stats', ticker)
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float_2(stats, 'high', 'max_price'),
            'low': self.safe_float_2(stats, 'low', 'min_price'),
            'bid': self.safe_float_2(ticker, 'best_bid_price', 'bid_price'),
            'bidVolume': self.safe_float(ticker, 'best_bid_amount'),
            'ask': self.safe_float_2(ticker, 'best_ask_price', 'ask_price'),
            'askVolume': self.safe_float(ticker, 'best_ask_amount'),
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': None,
            'quoteVolume': self.safe_float(stats, 'volume'),
            'info': ticker,
        }

    async def fetch_ticker(self, symbol, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        response = await self.publicGetTicker(self.extend(request, params))
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: {
        #             timestamp: 1583778859480,
        #             stats: {volume: 60627.57263769, low: 7631.5, high: 8311.5},
        #             state: 'open',
        #             settlement_price: 7903.21,
        #             open_interest: 111543850,
        #             min_price: 7634,
        #             max_price: 7866.51,
        #             mark_price: 7750.02,
        #             last_price: 7750.5,
        #             instrument_name: 'BTC-PERPETUAL',
        #             index_price: 7748.01,
        #             funding_8h: 0.0000026,
        #             current_funding: 0,
        #             best_bid_price: 7750,
        #             best_bid_amount: 19470,
        #             best_ask_price: 7750.5,
        #             best_ask_amount: 343280
        #         },
        #         usIn: 1583778859483941,
        #         usOut: 1583778859484075,
        #         usDiff: 134,
        #         testnet: False
        #     }
        #
        result = self.safe_value(response, 'result')
        return self.parse_ticker(result, market)

    async def fetch_tickers(self, symbols=None, params={}):
        await self.load_markets()
        code = self.code_from_options('fetchTickers')
        currency = self.currency(code)
        request = {
            'currency': currency['id'],
        }
        response = await self.publicGetGetBookSummaryByCurrency(self.extend(request, params))
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: [
        #             {
        #                 volume: 124.1,
        #                 underlying_price: 7856.445926872601,
        #                 underlying_index: 'SYN.BTC-10MAR20',
        #                 quote_currency: 'USD',
        #                 open_interest: 121.8,
        #                 mid_price: 0.01975,
        #                 mark_price: 0.01984559,
        #                 low: 0.0095,
        #                 last: 0.0205,
        #                 interest_rate: 0,
        #                 instrument_name: 'BTC-10MAR20-7750-C',
        #                 high: 0.0295,
        #                 estimated_delivery_price: 7856.29,
        #                 creation_timestamp: 1583783678366,
        #                 bid_price: 0.0185,
        #                 base_currency: 'BTC',
        #                 ask_price: 0.021
        #             },
        #         ],
        #         usIn: 1583783678361966,
        #         usOut: 1583783678372069,
        #         usDiff: 10103,
        #         testnet: False
        #     }
        #
        result = self.safe_value(response, 'result', [])
        tickers = {}
        for i in range(0, len(result)):
            ticker = self.parse_ticker(result[i])
            symbol = ticker['symbol']
            tickers[symbol] = ticker
        return self.filter_by_array(tickers, 'symbol', symbols)

    async def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
            'resolution': self.timeframes[timeframe],
        }
        duration = self.parse_timeframe(timeframe)
        now = self.milliseconds()
        if since is None:
            if limit is None:
                raise ArgumentsRequired(self.id + ' fetchOHLCV requires a since argument or a limit argument')
            else:
                request['start_timestamp'] = now - (limit - 1) * duration * 1000
                request['end_timestamp'] = now
        else:
            request['start_timestamp'] = since
            if limit is None:
                request['end_timestamp'] = now
            else:
                request['end_timestamp'] = self.sum(since, limit * duration * 1000)
        response = await self.publicGetGetTradingviewChartData(self.extend(request, params))
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: {
        #             volume: [3.6680847969999992, 22.682721123, 3.011587939, 0],
        #             ticks: [1583916960000, 1583917020000, 1583917080000, 1583917140000],
        #             status: 'ok',
        #             open: [7834, 7839, 7833.5, 7833],
        #             low: [7834, 7833.5, 7832.5, 7833],
        #             high: [7839.5, 7839, 7833.5, 7833],
        #             cost: [28740, 177740, 23590, 0],
        #             close: [7839.5, 7833.5, 7833, 7833]
        #         },
        #         usIn: 1583917166709801,
        #         usOut: 1583917166710175,
        #         usDiff: 374,
        #         testnet: False
        #     }
        #
        result = self.safe_value(response, 'result', {})
        ohlcvs = self.convert_trading_view_to_ohlcv(result, 'ticks', 'open', 'high', 'low', 'close', 'volume', True)
        return self.parse_ohlcvs(ohlcvs, market, timeframe, since, limit)

    def parse_trade(self, trade, market=None):
        #
        # fetchTrades(public)
        #
        #     {
        #         'trade_seq': 39201926,
        #         'trade_id':' 64135724',
        #         'timestamp': 1583174775400,
        #         'tick_direction': 1,
        #         'price': 8865.0,
        #         'instrument_name': 'BTC-PERPETUAL',
        #         'index_price': 8863.31,
        #         'direction': 'buy',
        #         'amount': 10.0
        #     }
        #
        # fetchMyTrades, fetchOrderTrades(private)
        #
        #     {
        #         "trade_seq": 3,
        #         "trade_id": "ETH-34066",
        #         "timestamp": 1550219814585,
        #         "tick_direction": 1,
        #         "state": "open",
        #         "self_trade": False,
        #         "reduce_only": False,
        #         "price": 0.04,
        #         "post_only": False,
        #         "order_type": "limit",
        #         "order_id": "ETH-334607",
        #         "matching_id": null,
        #         "liquidity": "M",
        #         "iv": 56.83,
        #         "instrument_name": "ETH-22FEB19-120-C",
        #         "index_price": 121.37,
        #         "fee_currency": "ETH",
        #         "fee": 0.0011,
        #         "direction": "buy",
        #         "amount": 11
        #     }
        #
        id = self.safe_string(trade, 'trade_id')
        symbol = None
        marketId = self.safe_string(trade, 'instrument_name')
        if marketId in self.markets_by_id:
            market = self.markets_by_id[marketId]
            symbol = market['symbol']
        if (symbol is None) and (market is not None):
            symbol = market['symbol']
        timestamp = self.safe_integer(trade, 'timestamp')
        side = self.safe_string(trade, 'direction')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'amount')
        cost = None
        if amount is not None:
            if price is not None:
                cost = amount * price
        liquidity = self.safe_string(trade, 'liquidity')
        takerOrMaker = None
        if liquidity is not None:
            # M = maker, T = taker, MT = both
            takerOrMaker = 'maker' if (liquidity == 'M') else 'taker'
        feeCost = self.safe_float(trade, 'fee')
        fee = None
        if feeCost is not None:
            feeCurrencyId = self.safe_string(trade, 'fee_currency')
            feeCurrencyCode = self.safe_currency_code(feeCurrencyId)
            fee = {
                'cost': feeCost,
                'currency': feeCurrencyCode,
            }
        return {
            'id': id,
            'info': trade,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'order': self.safe_string(trade, 'order_id'),
            'type': self.safe_string(trade, 'order_type'),
            'side': side,
            'takerOrMaker': takerOrMaker,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': fee,
        }

    async def fetch_trades(self, symbol, since=None, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
            'include_old': True,
        }
        method = 'publicGetGetLastTradesByInstrument' if (
                    since is None) else 'publicGetGetLastTradesByInstrumentAndTime'
        if since is not None:
            request['start_timestamp'] = since
        if limit is not None:
            request['count'] = limit  # default 10
        response = await getattr(self, method)(self.extend(request, params))
        #
        #     {
        #         'jsonrpc': '2.0',
        #         'result': {
        #             'trades': [
        #                 {
        #                     'trade_seq': 39201926,
        #                     'trade_id':' 64135724',
        #                     'timestamp': 1583174775400,
        #                     'tick_direction': 1,
        #                     'price': 8865.0,
        #                     'instrument_name': 'BTC-PERPETUAL',
        #                     'index_price': 8863.31,
        #                     'direction': 'buy',
        #                     'amount': 10.0
        #                 },
        #             ],
        #             'has_more': True,
        #         },
        #         'usIn': 1583779594843931,
        #         'usOut': 1583779594844446,
        #         'usDiff': 515,
        #         'testnet': False
        #     }
        #
        result = self.safe_value(response, 'result', {})
        trades = self.safe_value(result, 'trades', [])
        return self.parse_trades(trades, market, since, limit)

    async def fetch_order_book(self, symbol, limit=None, params={}):
        await self.load_markets()
        market = self.market(symbol)
        request = {
            'instrument_name': market['id'],
        }
        if limit is not None:
            request['depth'] = limit
        response = await self.publicGetGetOrderBook(self.extend(request, params))
        #
        #     {
        #         jsonrpc: '2.0',
        #         result: {
        #             timestamp: 1583781354740,
        #             stats: {volume: 61249.66735634, low: 7631.5, high: 8311.5},
        #             state: 'open',
        #             settlement_price: 7903.21,
        #             open_interest: 111536690,
        #             min_price: 7695.13,
        #             max_price: 7929.49,
        #             mark_price: 7813.06,
        #             last_price: 7814.5,
        #             instrument_name: 'BTC-PERPETUAL',
        #             index_price: 7810.12,
        #             funding_8h: 0.0000031,
        #             current_funding: 0,
        #             change_id: 17538025952,
        #             bids: [
        #                 [7814, 351820],
        #                 [7813.5, 207490],
        #                 [7813, 32160],
        #             ],
        #             best_bid_price: 7814,
        #             best_bid_amount: 351820,
        #             best_ask_price: 7814.5,
        #             best_ask_amount: 11880,
        #             asks: [
        #                 [7814.5, 11880],
        #                 [7815, 18100],
        #                 [7815.5, 2640],
        #             ],
        #         },
        #         usIn: 1583781354745804,
        #         usOut: 1583781354745932,
        #         usDiff: 128,
        #         testnet: False
        #     }
        #
        result = self.safe_value(response, 'result', {})
        timestamp = self.safe_integer(result, 'timestamp')
        nonce = self.safe_integer(result, 'change_id')
        orderbook = self.parse_order_book(result, timestamp)
        orderbook['nonce'] = nonce
        return orderbook
