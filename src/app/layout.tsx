import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { ThemeProvider } from "@/shared/components/theme-provider";
import { JsonLd } from "@/shared/components/json-ld";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  metadataBase: new URL('https://tensor-track.vercel.app'),
  title: {
    default: 'TensorTrack — AI Engineer Prep & Upskilling',
    template: '%s | TensorTrack',
  },
  description: 'Master AI engineering from first principles. A structured, gamified curriculum covering Python, ML, Deep Learning, LLMs, RAG, AI Agents, and System Design — with curated resources and XP tracking.',
  keywords: [
    'AI engineer roadmap',
    'learn AI engineering',
    'LLM engineer',
    'machine learning roadmap',
    'AI engineer interview prep',
    'deep learning curriculum',
    'RAG system design',
    'AI agents learning',
  ],
  authors: [{ name: 'TensorTrack' }],
  alternates: {
    canonical: 'https://tensor-track.vercel.app',
  },
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://tensor-track.vercel.app',
    siteName: 'TensorTrack',
    title: 'TensorTrack — AI Engineer Prep & Upskilling',
    description: 'Master AI engineering from first principles. Structured curriculum, gamified XP, 100+ curated resources.',
    images: [
      {
        url: '/og-image.png',
        width: 1200,
        height: 630,
        alt: 'TensorTrack — AI Engineer Roadmap',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'TensorTrack — AI Engineer Prep & Upskilling',
    description: 'Master AI engineering from first principles.',
    images: ['/og-image.png'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  verification: {
    google: '4K9KQwXmaycyqJ8k5XFxwk_4H1k2PQytG7UPj0jCDp8',
  },
};

const websiteSchema = {
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "TensorTrack",
  "url": "https://tensor-track.vercel.app",
  "description": "Structured AI engineering learning platform with gamified curriculum and curated resources.",
  "potentialAction": {
    "@type": "SearchAction",
    "target": "https://tensor-track.vercel.app/learning-items?q={search_term_string}",
    "query-input": "required name=search_term_string"
  }
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
      suppressHydrationWarning
    >
      <head>
        <JsonLd data={websiteSchema} />
      </head>
      <body className="min-h-full flex flex-col bg-background text-foreground bg-grid-pattern">
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          enableSystem
          disableTransitionOnChange
        >
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
