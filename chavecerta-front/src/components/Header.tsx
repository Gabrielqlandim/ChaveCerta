/**
 * Componente Header do ChaveCerta
 * 
 * Header responsivo com navegação principal, logo e ações do usuário.
 * Inclui busca rápida e menu mobile.
 */

'use client';

import { useState } from 'react';
import Link from 'next/link';
import { Search, Menu, X, User, Heart } from 'lucide-react';

interface HeaderProps {
  className?: string;
}

/**
 * Componente Header principal da aplicação
 */
export default function Header({ className = '' }: HeaderProps) {
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [isSearchOpen, setIsSearchOpen] = useState(false);

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  const toggleSearch = () => {
    setIsSearchOpen(!isSearchOpen);
  };

  return (
    <header className={`bg-white shadow-sm border-b border-gray-100 sticky top-0 z-50 ${className}`}>
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex-shrink-0">
            <Link href="/" className="flex items-center space-x-2">
              <div className="w-10 h-10 bg-blue-600 rounded-xl flex items-center justify-center">
                <span className="text-white font-bold text-lg">C</span>
              </div>
              <span className="text-xl font-bold text-gray-900 hidden sm:block">
                ChaveCerta
              </span>
            </Link>
          </div>

          {/* Navegação Desktop */}
          <nav className="hidden md:flex items-center space-x-8">
            <Link 
              href="/imoveis" 
              className="text-gray-700 hover:text-blue-600 font-medium transition-colors"
            >
              Imóveis
            </Link>
            <Link 
              href="/sobre" 
              className="text-gray-700 hover:text-blue-600 font-medium transition-colors"
            >
              Sobre
            </Link>
            <Link 
              href="/contato" 
              className="text-gray-700 hover:text-blue-600 font-medium transition-colors"
            >
              Contato
            </Link>
          </nav>

          {/* Busca e Ações */}
          <div className="flex items-center space-x-4">
            {/* Busca Desktop */}
            <div className="hidden lg:flex items-center">
              <div className="relative">
                <input
                  type="text"
                  placeholder="Buscar imóveis..."
                  className="w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
                <Search className="absolute left-3 top-2.5 h-5 w-5 text-gray-400" />
              </div>
            </div>

            {/* Busca Mobile */}
            <button
              onClick={toggleSearch}
              className="lg:hidden p-2 text-gray-700 hover:text-blue-600 transition-colors"
            >
              <Search className="h-5 w-5" />
            </button>

            {/* Favoritos */}
            <Link
              href="/favoritos"
              className="p-2 text-gray-700 hover:text-blue-600 transition-colors"
            >
              <Heart className="h-5 w-5" />
            </Link>

            {/* Perfil do Usuário */}
            <div className="relative">
              <button className="flex items-center space-x-2 p-2 text-gray-700 hover:text-blue-600 transition-colors">
                <User className="h-5 w-5" />
                <span className="hidden sm:block text-sm font-medium">Entrar</span>
              </button>
            </div>

            {/* Menu Mobile */}
            <button
              onClick={toggleMobileMenu}
              className="md:hidden p-2 text-gray-700 hover:text-blue-600 transition-colors"
            >
              {isMobileMenuOpen ? (
                <X className="h-5 w-5" />
              ) : (
                <Menu className="h-5 w-5" />
              )}
            </button>
          </div>
        </div>

        {/* Menu Mobile */}
        {isMobileMenuOpen && (
          <div className="md:hidden border-t border-gray-100">
            <div className="px-2 pt-2 pb-3 space-y-1">
              <Link
                href="/imoveis"
                className="block px-3 py-2 text-gray-700 hover:text-blue-600 font-medium"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                Imóveis
              </Link>
              <Link
                href="/sobre"
                className="block px-3 py-2 text-gray-700 hover:text-blue-600 font-medium"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                Sobre
              </Link>
              <Link
                href="/contato"
                className="block px-3 py-2 text-gray-700 hover:text-blue-600 font-medium"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                Contato
              </Link>
            </div>
          </div>
        )}

        {/* Busca Mobile Expandida */}
        {isSearchOpen && (
          <div className="lg:hidden border-t border-gray-100 p-4">
            <div className="relative">
              <input
                type="text"
                placeholder="Buscar imóveis..."
                className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
              />
              <Search className="absolute left-3 top-2.5 h-5 w-5 text-gray-400" />
            </div>
          </div>
        )}
      </div>
    </header>
  );
}
