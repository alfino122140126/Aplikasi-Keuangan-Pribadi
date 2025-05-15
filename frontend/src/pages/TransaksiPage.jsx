import { useEffect, useState } from 'react';
import { api } from '../services/api';

export default function TransaksiPage() {
  const [data, setData] = useState([]);

  useEffect(() => {
    api.get('/transaksi').then(res => setData(res.data));
  }, []);

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold">Data Transaksi</h2>
      <ul className="mt-4 space-y-2">
        {data.map((t) => (
          <li key={t.id} className="border p-2">{t.kategori} - {t.jumlah} - {t.tanggal}</li>
        ))}
      </ul>
    </div>
  );
}