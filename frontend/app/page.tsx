"use client";

import { useEffect, useState } from "react";
import api from "@/lib/api";

import {
  Card,
  CardContent,
} from "@/components/ui/card";

type DashboardData = {
  total_records: number;
  pending_reviews: number;
  approved_records: number;
  suspicious_records: number;
};

export default function DashboardPage() {

  const [data, setData] =
    useState<DashboardData | null>(null);

  useEffect(() => {

    api
      .get("/emissions/dashboard-summary/")
      .then((res) => setData(res.data));

  }, []);

  if (!data) {
    return (
      <div className="p-10">
        Loading...
      </div>
    );
  }

  return (
    <main className="p-10">

      <h1 className="text-4xl font-bold mb-8">
        Dashboard
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-muted-foreground">
              Total Records
            </p>

            <h2 className="text-3xl font-bold">
              {data.total_records}
            </h2>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-muted-foreground">
              Pending Reviews
            </p>

            <h2 className="text-3xl font-bold">
              {data.pending_reviews}
            </h2>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-muted-foreground">
              Approved Records
            </p>

            <h2 className="text-3xl font-bold">
              {data.approved_records}
            </h2>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <p className="text-sm text-muted-foreground">
              Suspicious Records
            </p>

            <h2 className="text-3xl font-bold">
              {data.suspicious_records}
            </h2>
          </CardContent>
        </Card>

      </div>

    </main>
  );
}