"use client";

import Link from "next/link";

export default function Sidebar() {

  return (

    <div className="w-64 min-h-screen border-r p-6 bg-muted/40">

      <h1 className="text-2xl font-bold mb-10">
        ESG
      </h1>

      <nav className="space-y-4">

        <Link
          href="/"
          className="block hover:underline"
        >
          Dashboard
        </Link>

        <Link
          href="/upload"
          className="block hover:underline"
        >
          Upload Data
        </Link>

        <Link
          href="/review"
          className="block hover:underline"
        >
          Review Queue
        </Link>

      </nav>

    </div>
  );
}