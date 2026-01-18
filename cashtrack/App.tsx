import { View, Text } from "react-native";
import { useEffect, useState } from "react";

type Transaction = {
  id: number;
  amount: number;
  note?: string;
};

export default function App() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);

  useEffect(() => {
    fetch("http://192.168.1.3:8000/transactions")
      .then(res => res.json())
      .then(data => {
        console.log("TRANSACTIONS:", data);
        setTransactions(data);
      })
      .catch(err => {
        console.log("ERROR:", err);
      });
  }, []);

  return (
    <View style={{ padding: 20 }}>
      <Text>Daftar Transaksi:</Text>

      {transactions.map(tx => (
        <View key={tx.id}>
          <Text>Rp {tx.amount}</Text>
          <Text>{tx.note}</Text>
        </View>
      ))}
    </View>
  );
}
