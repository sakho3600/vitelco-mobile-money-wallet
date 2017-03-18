from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from app_dir.wallet_transactions.models import BatchTransaction
from app_dir.wallet_transactions.serializers import BatchTransactionSerializer


class APIRootView(APIView):
    def get(self, request):
        api_registry = {
            "Transactions": {
                "Get transaction by transaction_reference": reverse(
                    "get_transaction_by_transaction_reference",
                    request=request,
                    current_app="wallet_transactions",
                    kwargs={
                        "transaction_reference":
                            "753bcd19-7230-40ba-a975-09ac94ace0d2"
                    }


                )

            },
            "BatchTransactions": {
                "Create batch transactions": reverse(
                    "batchtransactions", request=request
                )
            },
            "Account": {
                "Get Account status by msisdn": reverse(
                    "account:msisdn",
                    request=request,
                    current_app="customer_wallet_management",
                    kwargs={"msisdn": "+254711111111"}
                ),
                "Get Account status by accountId": reverse(
                    "account:get_account_status_by_account_id",
                    request=request,
                    current_app="customer_wallet_management",
                    kwargs={
                        "wallet_id": "753bcd19-7230-40ba-a975-09ac94ace0d2"
                    }
                ),
                "Get Account name by msisdn": reverse(
                    "account:get_account_name_by_msisdn",
                    request=request,
                    current_app="customer_wallet_management",
                    kwargs={"msisdn": "254711111111"}
                ),
                "Get Account name by accountId": reverse(
                        "account:get_account_name_by_account_id",
                        request=request,
                        current_app="customer_wallet_management",
                        kwargs={"account_id":
                                    "753bcd19-7230-40ba-a975-09ac94ace0d2"}
                ),
                "Get Account balance by msisdn": reverse(
                    "account:get_account_balance_by_msisdn",
                    request=request,
                    current_app="customer_wallet_management",
                    kwargs={"msisdn": "254711111111"}
                ),
                "Get Account balance by accountId": reverse(
                    "account:get_account_balance_by_account_id",
                    request=request,
                    current_app="customer_wallet_management",
                    kwargs={"account_id":
                                "753bcd19-7230-40ba-a975-09ac94ace0d2"}
                ),


            },
            "Notification": {
                "ListCreate Notifications": reverse(
                    "notify:notifications",
                    request=request,
                    current_app="notification_management"
                )
            }
        }
        return Response(api_registry)


class BatchTransactions(APIView):

    def get_object(self, pk):
        try:
            return BatchTransaction.objects.get(pk=pk)
        except BatchTransaction.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        bulk_transactions = BatchTransaction.objects.all()
        serializer = BatchTransactionSerializer(bulk_transactions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):



        serializer = BatchTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)