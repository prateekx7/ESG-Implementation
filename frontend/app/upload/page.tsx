"use client";

import { useState } from "react";
import api from "@/lib/api";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function UploadPage() {

  const [file, setFile] =
    useState<File | null>(null);

  const [sourceType, setSourceType] =
    useState("sap");

  const [message, setMessage] =
    useState("");

  const handleUpload = async () => {

    if (!file) return;

    const formData = new FormData();

    formData.append("organization_id", "1");

    formData.append("source_type", sourceType);

    formData.append("file", file);

    try {

      const res = await api.post(
        "/ingestion/upload/",
        formData
      );

      setMessage(
        JSON.stringify(res.data)
      );

    } catch (err) {

      setMessage("Upload failed");

    }
  };

  return (

    <main className="p-10 max-w-xl">

      <h1 className="text-4xl font-bold mb-8">
        Upload Data Source
      </h1>

      <div className="space-y-4">

        <select
          className="border rounded p-2 w-full"
          value={sourceType}
          onChange={(e) =>
            setSourceType(e.target.value)
          }
        >
          <option value="sap">
            SAP
          </option>

          <option value="utility">
            Utility
          </option>

          <option value="travel">
            Travel
          </option>

        </select>

        <Input
          type="file"
          onChange={(e) => {

            if (e.target.files?.[0]) {
              setFile(e.target.files[0]);
            }

          }}
        />

        <Button onClick={handleUpload}>
          Upload CSV
        </Button>

        <p>{message}</p>

      </div>

    </main>
  );
}