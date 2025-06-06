/**
 * Layout principal do ChaveCerta
 * 
 * Define a estrutura base da aplicação com:
 * - Metadados SEO
 * - Fontes otimizadas
 * - Configurações globais
 */

import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "ChaveCerta - Aluguel de Imóveis",
  description: "A plataforma mais completa para aluguel de imóveis no Brasil. Encontre apartamentos, casas, kitnets e imóveis comerciais com segurança e praticidade.",
  keywords: ["aluguel", "imóveis", "apartamento", "casa", "kitnet", "comercial", "locação"],
  authors: [{ name: "ChaveCerta" }],
  creator: "ChaveCerta",
  publisher: "ChaveCerta",
  robots: "index, follow",
  openGraph: {
    type: "website",
    locale: "pt_BR",
    url: "https://chavecerta.com.br",
    title: "ChaveCerta - Aluguel de Imóveis",
    description: "A plataforma mais completa para aluguel de imóveis no Brasil.",
    siteName: "ChaveCerta",
  },
  twitter: {
    card: "summary_large_image",
    title: "ChaveCerta - Aluguel de Imóveis",
    description: "A plataforma mais completa para aluguel de imóveis no Brasil.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body className={`${inter.className} antialiased`}>
        {children}
      </body>
    </html>
  );
}
