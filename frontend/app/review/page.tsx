"use client";

import {
  useEffect,
  useState,
} from "react";

import api from "@/lib/api";

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";

import { Button } from "@/components/ui/button";

type RecordType = {
  id: number;
  category: string;
  activity_value: number;
  co2e_emissions: number;
  suspicious: boolean;
};

export default function ReviewPage() {

  const [records, setRecords] =
    useState<RecordType[]>([]);

  const fetchRecords = () => {

    api
      .get("/emissions/pending/")
      .then((res) => setRecords(res.data));

  };

  useEffect(() => {

    fetchRecords();

  }, []);

  const approveRecord = async (
    id: number
  ) => {

    await api.post(
      `/emissions/approve/${id}/`
    );

    fetchRecords();
  };

  const rejectRecord = async (
    id: number
  ) => {

    await api.post(
      `/emissions/reject/${id}/`
    );

    fetchRecords();
  };

  return (

    <main className="p-10">

      <h1 className="text-4xl font-bold mb-8">
        Pending Review Queue
      </h1>

      <Table>

        <TableHeader>

          <TableRow>
            <TableHead>ID</TableHead>
            <TableHead>Category</TableHead>
            <TableHead>Value</TableHead>
            <TableHead>CO2e</TableHead>
            <TableHead>Suspicious</TableHead>
            <TableHead>Actions</TableHead>
          </TableRow>

        </TableHeader>

        <TableBody>

          {records.map((record) => (

            <TableRow key={record.id}>

              <TableCell>
                {record.id}
              </TableCell>

              <TableCell>
                {record.category}
              </TableCell>

              <TableCell>
                {record.activity_value}
              </TableCell>

              <TableCell>
                {record.co2e_emissions}
              </TableCell>

              <TableCell>
                <span
                  className={
                    record.suspicious
                      ? "text-red-500 font-semibold"
                      : "text-green-600"
                  }
                >
                  {record.suspicious
                    ? "Flagged"
                    : "Clean"}
                </span>
              </TableCell>

              <TableCell className="space-x-2">

                <Button
                  onClick={() =>
                    approveRecord(record.id)
                  }
                >
                  Approve
                </Button>

                <Button
                  variant="destructive"
                  onClick={() =>
                    rejectRecord(record.id)
                  }
                >
                  Reject
                </Button>

              </TableCell>

            </TableRow>

          ))}

        </TableBody>

      </Table>

    </main>
  );
}