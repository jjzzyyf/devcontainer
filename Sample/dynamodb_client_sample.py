class DynamoDBClientSample:

    def __init__(self, client, table_name, pk):
        self.client = client
        self.table_name = table_name
        self.pk = pk

    def create_table(self):
        """Create a dynamodb table

        Reference:
            https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/create_table.html

        Table name: sample
        Partition key: ID

        Required Parameters:
            TableName
            KeySchema
            AttributeDefinitions
            BillingMode or ProvisionedThroughput
        """

        response = self.client.create_table(
            AttributeDefinitions=[{"AttributeName": self.pk, "AttributeType": "S"}],
            TableName=self.table_name,
            KeySchema=[{"AttributeName": self.pk, "KeyType": "HASH"}],
            BillingMode="PAY_PER_REQUEST",
        )
        return response

    def put_item(self, pk_value: str, name: str, age: str):
        """Put some items into the table

        https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/put_item.html

        Required Parameters:
            TableName
            Item
                Partition key
        """
        response = self.client.put_item(
            TableName=self.table_name,
            Item={self.pk: {"S": pk_value}, "Name": {"S": name}, "Age": {"S": age}},
        )
        return response

    def scan_table(self):
        """Scan the table

        Reference:
            https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/scan.html

        Required Parameters:
            TableName
        """

        response = self.client.scan(TableName=self.table_name)
        return response

    def query_table(self, pk_value: str):
        """Query the table

        Reference:
            https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/query.html

        Required Parameters:
            TableName
            KeyConditionExpression
            ExpressionAttributeValues
        """

        response = self.client.query(
            TableName=self.table_name,
            KeyConditionExpression=f"{self.pk} = :pk_value",
            ExpressionAttributeValues={":pk_value": {"S": pk_value}},
        )
        return response

    def delete_table(self):
        try:
            self.client.delete_table(TableName=self.table_name)
        except self.client.exceptions.ResourceNotFoundException:
            pass
