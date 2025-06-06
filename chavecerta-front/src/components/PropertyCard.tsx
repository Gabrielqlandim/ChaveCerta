/**
 * Componente PropertyCard do ChaveCerta
 * 
 * Card responsivo para exibir informações de imóveis.
 * Suporta layout em grid e lista com funcionalidade de favoritos.
 */

'use client';

import { useState } from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { Heart, MapPin, Bed, Bath, Car, Square } from 'lucide-react';
import { PropertyCardProps } from '@/types';

/**
 * Componente de card para exibir imóveis
 */
export default function PropertyCard({
  imovel,
  variant = 'grid',
  showFavorite = true,
  onFavoriteClick
}: PropertyCardProps) {
  const [isFavorited, setIsFavorited] = useState(false);
  const [imageError, setImageError] = useState(false);

  const handleFavoriteClick = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsFavorited(!isFavorited);
    onFavoriteClick?.(imovel.id);
  };

  const formatPrice = (price: number) => {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    }).format(price);
  };

  const primaryImage = imovel.imagens?.[0] || '/placeholder-property.jpg';

  // Layout em grid (padrão)
  if (variant === 'grid') {
    return (
      <Link href={`/imoveis/${imovel.id}`}>
        <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-all duration-300 group">
          {/* Imagem */}
          <div className="relative h-48 overflow-hidden">
            <Image
              src={imageError ? '/placeholder-property.jpg' : primaryImage}
              alt={imovel.titulo}
              fill
              className="object-cover group-hover:scale-105 transition-transform duration-300"
              onError={() => setImageError(true)}
            />
            
            {/* Badge de tipo */}
            <div className="absolute top-3 left-3">
              <span className="bg-blue-600 text-white text-xs font-medium px-2 py-1 rounded-full">
                {imovel.tipo}
              </span>
            </div>

            {/* Botão de favorito */}
            {showFavorite && (
              <button
                onClick={handleFavoriteClick}
                className="absolute top-3 right-3 p-2 bg-white rounded-full shadow-sm hover:shadow-md transition-all"
              >
                <Heart
                  className={`h-4 w-4 ${
                    isFavorited ? 'fill-red-500 text-red-500' : 'text-gray-600'
                  }`}
                />
              </button>
            )}

            {/* Badge de disponibilidade */}
            {!imovel.disponivel && (
              <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center">
                <span className="text-white font-semibold text-lg">Indisponível</span>
              </div>
            )}
          </div>

          {/* Conteúdo */}
          <div className="p-4">
            {/* Preço */}
            <div className="flex items-center justify-between mb-2">
              <span className="text-2xl font-bold text-gray-900">
                {formatPrice(imovel.preco_mensal)}
              </span>
              <span className="text-sm text-gray-500">/mês</span>
            </div>

            {/* Título */}
            <h3 className="font-semibold text-gray-900 mb-2 line-clamp-2">
              {imovel.titulo}
            </h3>

            {/* Localização */}
            <div className="flex items-center text-gray-600 mb-3">
              <MapPin className="h-4 w-4 mr-1" />
              <span className="text-sm line-clamp-1">
                {imovel.cidade}, {imovel.estado}
              </span>
            </div>

            {/* Características */}
            <div className="flex items-center justify-between text-sm text-gray-600">
              <div className="flex items-center space-x-3">
                <div className="flex items-center">
                  <Bed className="h-4 w-4 mr-1" />
                  <span>{imovel.quartos}</span>
                </div>
                <div className="flex items-center">
                  <Bath className="h-4 w-4 mr-1" />
                  <span>{imovel.banheiros}</span>
                </div>
                <div className="flex items-center">
                  <Car className="h-4 w-4 mr-1" />
                  <span>{imovel.vagas_garagem}</span>
                </div>
              </div>
              <div className="flex items-center">
                <Square className="h-4 w-4 mr-1" />
                <span>{imovel.area_m2}m²</span>
              </div>
            </div>

            {/* Tags */}
            {(imovel.mobiliado || imovel.permite_pets) && (
              <div className="flex flex-wrap gap-1 mt-3">
                {imovel.mobiliado && (
                  <span className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full">
                    Mobiliado
                  </span>
                )}
                {imovel.permite_pets && (
                  <span className="bg-orange-100 text-orange-800 text-xs px-2 py-1 rounded-full">
                    Pet Friendly
                  </span>
                )}
              </div>
            )}
          </div>
        </div>
      </Link>
    );
  }

  // Layout em lista
  return (
    <Link href={`/imoveis/${imovel.id}`}>
      <div className="bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden hover:shadow-md transition-all duration-300 group">
        <div className="flex flex-col sm:flex-row">
          {/* Imagem */}
          <div className="relative h-48 sm:h-32 sm:w-48 flex-shrink-0 overflow-hidden">
            <Image
              src={imageError ? '/placeholder-property.jpg' : primaryImage}
              alt={imovel.titulo}
              fill
              className="object-cover group-hover:scale-105 transition-transform duration-300"
              onError={() => setImageError(true)}
            />
            
            {/* Badge de tipo */}
            <div className="absolute top-2 left-2">
              <span className="bg-blue-600 text-white text-xs font-medium px-2 py-1 rounded-full">
                {imovel.tipo}
              </span>
            </div>

            {/* Botão de favorito */}
            {showFavorite && (
              <button
                onClick={handleFavoriteClick}
                className="absolute top-2 right-2 p-1.5 bg-white rounded-full shadow-sm hover:shadow-md transition-all"
              >
                <Heart
                  className={`h-3 w-3 ${
                    isFavorited ? 'fill-red-500 text-red-500' : 'text-gray-600'
                  }`}
                />
              </button>
            )}
          </div>

          {/* Conteúdo */}
          <div className="flex-1 p-4">
            <div className="flex flex-col sm:flex-row sm:justify-between">
              <div className="flex-1">
                {/* Título e preço */}
                <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between mb-2">
                  <h3 className="font-semibold text-gray-900 mb-1 sm:mb-0 line-clamp-1">
                    {imovel.titulo}
                  </h3>
                  <div className="text-right">
                    <span className="text-xl font-bold text-gray-900">
                      {formatPrice(imovel.preco_mensal)}
                    </span>
                    <span className="text-sm text-gray-500">/mês</span>
                  </div>
                </div>

                {/* Localização */}
                <div className="flex items-center text-gray-600 mb-2">
                  <MapPin className="h-4 w-4 mr-1" />
                  <span className="text-sm">
                    {imovel.cidade}, {imovel.estado}
                  </span>
                </div>

                {/* Características */}
                <div className="flex items-center justify-between">
                  <div className="flex items-center space-x-4 text-sm text-gray-600">
                    <div className="flex items-center">
                      <Bed className="h-4 w-4 mr-1" />
                      <span>{imovel.quartos} quartos</span>
                    </div>
                    <div className="flex items-center">
                      <Bath className="h-4 w-4 mr-1" />
                      <span>{imovel.banheiros} banheiros</span>
                    </div>
                    <div className="flex items-center">
                      <Square className="h-4 w-4 mr-1" />
                      <span>{imovel.area_m2}m²</span>
                    </div>
                  </div>

                  {/* Tags */}
                  <div className="flex gap-1">
                    {imovel.mobiliado && (
                      <span className="bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full">
                        Mobiliado
                      </span>
                    )}
                    {imovel.permite_pets && (
                      <span className="bg-orange-100 text-orange-800 text-xs px-2 py-1 rounded-full">
                        Pet Friendly
                      </span>
                    )}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Link>
  );
}
