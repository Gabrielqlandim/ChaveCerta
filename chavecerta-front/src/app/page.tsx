/**
 * Página Principal do ChaveCerta
 * 
 * Landing page moderna com seções organizadas:
 * - Hero section com busca
 * - Tipos de propriedades
 * - Imóveis em destaque
 * - Estatísticas
 * - Recursos e benefícios
 * - Call-to-action
 */

'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { 
  Search, 
  Home as HomeIcon, 
  Building, 
  Store, 
  Users, 
  TrendingUp, 
  Shield,
  Clock,
  Award,
  ArrowRight,
  Star,
  MapPin
} from 'lucide-react';

import Header from '@/components/Header';
import PropertyCard from '@/components/PropertyCard';
import { Imovel, SearchFormData, HomeStats, PropertyType } from '@/types';

/**
 * Componente da página inicial
 */
export default function Home() {
  const [searchData, setSearchData] = useState<SearchFormData>({
    cidade: '',
    tipo: '',
    precoMin: undefined,
    precoMax: undefined,
    quartos: undefined
  });

  // Mock data para demonstração
  const featuredProperties: Imovel[] = [
    {
      id: 1,
      titulo: 'Apartamento Moderno no Centro',
      descricao: 'Lindo apartamento com vista para a cidade',
      tipo: 'apartamento',
      endereco: 'Rua das Flores, 123',
      cidade: 'São Paulo',
      estado: 'SP',
      cep: '01234-567',
      preco_mensal: 2500,
      area_m2: 75,
      quartos: 2,
      banheiros: 2,
      vagas_garagem: 1,
      mobiliado: true,
      permite_pets: false,
      disponivel: true,
      created_at: '2024-01-01',
      updated_at: '2024-01-01',
      proprietario: {
        id: 1,
        email: 'proprietario@email.com',
        nome: 'João Silva',
        tipo_usuario: 'proprietario',
        is_active: true,
        created_at: '2024-01-01',
        updated_at: '2024-01-01'
      },
      imagens: ['/placeholder-property.jpg'],
      amenidades: ['Academia', 'Piscina', 'Portaria 24h']
    },
    {
      id: 2,
      titulo: 'Casa Aconchegante com Jardim',
      descricao: 'Casa familiar com amplo jardim',
      tipo: 'casa',
      endereco: 'Rua dos Jasmins, 456',
      cidade: 'Rio de Janeiro',
      estado: 'RJ',
      cep: '22000-000',
      preco_mensal: 3200,
      area_m2: 120,
      quartos: 3,
      banheiros: 2,
      vagas_garagem: 2,
      mobiliado: false,
      permite_pets: true,
      disponivel: true,
      created_at: '2024-01-01',
      updated_at: '2024-01-01',
      proprietario: {
        id: 2,
        email: 'maria@email.com',
        nome: 'Maria Santos',
        tipo_usuario: 'proprietario',
        is_active: true,
        created_at: '2024-01-01',
        updated_at: '2024-01-01'
      },
      imagens: ['/placeholder-property.jpg'],
      amenidades: ['Jardim', 'Churrasqueira', 'Garagem']
    },
    {
      id: 3,
      titulo: 'Kitnet Prática para Estudantes',
      descricao: 'Perfeita para estudantes universitários',
      tipo: 'kitnet',
      endereco: 'Rua Universitária, 789',
      cidade: 'Belo Horizonte',
      estado: 'MG',
      cep: '30000-000',
      preco_mensal: 800,
      area_m2: 25,
      quartos: 1,
      banheiros: 1,
      vagas_garagem: 0,
      mobiliado: true,
      permite_pets: false,
      disponivel: true,
      created_at: '2024-01-01',
      updated_at: '2024-01-01',
      proprietario: {
        id: 3,
        email: 'carlos@email.com',
        nome: 'Carlos Oliveira',
        tipo_usuario: 'proprietario',
        is_active: true,
        created_at: '2024-01-01',
        updated_at: '2024-01-01'
      },
      imagens: ['/placeholder-property.jpg'],
      amenidades: ['Mobiliado', 'Internet', 'Próximo à universidade']
    }
  ];

  const homeStats: HomeStats = {
    totalImoveis: 1247,
    totalProprietarios: 458,
    totalContratos: 892,
    mediaPreco: 2150
  };

  const propertyTypes: PropertyType[] = [
    {
      tipo: 'apartamento',
      nome: 'Apartamentos',
      descricao: 'Modernos e bem localizados',
      icone: 'building',
      quantidade: 542
    },
    {
      tipo: 'casa',
      nome: 'Casas',
      descricao: 'Conforto e privacidade',
      icone: 'home',
      quantidade: 387
    },
    {
      tipo: 'kitnet',
      nome: 'Kitnets',
      descricao: 'Práticas e econômicas',
      icone: 'home',
      quantidade: 248
    },
    {
      tipo: 'comercial',
      nome: 'Comerciais',
      descricao: 'Para seu negócio crescer',
      icone: 'store',
      quantidade: 70
    }
  ];

  /**
   * Manipula a busca de imóveis
   */
  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Buscar:', searchData);
    // Aqui seria feita a navegação para a página de resultados
  };

  /**
   * Renderiza o ícone do tipo de propriedade
   */
  const getPropertyTypeIcon = (iconType: string) => {
    switch (iconType) {
      case 'building':
        return <Building className="h-8 w-8" />;
      case 'home':
        return <HomeIcon className="h-8 w-8" />;
      case 'store':
        return <Store className="h-8 w-8" />;
      default:
        return <HomeIcon className="h-8 w-8" />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      
      {/* Hero Section */}
      <section className="relative bg-gradient-to-br from-blue-600 to-blue-800 text-white py-20">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="max-w-4xl mx-auto text-center">
            {/* Título Principal */}
            <h1 className="text-4xl md:text-6xl font-bold mb-6">
              Encontre o <span className="text-blue-200">imóvel perfeito</span> para você
            </h1>
            
            <p className="text-xl md:text-2xl mb-12 text-blue-100">
              A plataforma mais completa para aluguel de imóveis no Brasil
            </p>

            {/* Formulário de Busca */}
            <div className="bg-white rounded-xl p-6 shadow-xl">
              <form onSubmit={handleSearch} className="flex flex-col md:flex-row gap-4">
                <div className="flex-1">
                  <input
                    type="text"
                    placeholder="Cidade ou região"
                    value={searchData.cidade}
                    onChange={(e) => setSearchData({ ...searchData, cidade: e.target.value })}
                    className="w-full px-4 py-3 rounded-lg border border-gray-300 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  />
                </div>
                
                <div className="flex-1">
                  <select
                    value={searchData.tipo}
                    onChange={(e) => setSearchData({ ...searchData, tipo: e.target.value })}
                    className="w-full px-4 py-3 rounded-lg border border-gray-300 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="">Tipo de imóvel</option>
                    <option value="apartamento">Apartamento</option>
                    <option value="casa">Casa</option>
                    <option value="kitnet">Kitnet</option>
                    <option value="comercial">Comercial</option>
                  </select>
                </div>
                
                <div className="flex-1">
                  <select
                    value={searchData.quartos}
                    onChange={(e) => setSearchData({ ...searchData, quartos: e.target.value ? parseInt(e.target.value) : undefined })}
                    className="w-full px-4 py-3 rounded-lg border border-gray-300 text-gray-900 focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  >
                    <option value="">Quartos</option>
                    <option value="1">1 quarto</option>
                    <option value="2">2 quartos</option>
                    <option value="3">3 quartos</option>
                    <option value="4">4+ quartos</option>
                  </select>
                </div>
                
                <button
                  type="submit"
                  className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg font-semibold transition-colors flex items-center justify-center gap-2"
                >
                  <Search className="h-5 w-5" />
                  Buscar
                </button>
              </form>
            </div>
          </div>
        </div>
      </section>

      {/* Estatísticas */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                {homeStats.totalImoveis.toLocaleString()}
              </div>
              <div className="text-gray-600">Imóveis Disponíveis</div>
            </div>
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                {homeStats.totalProprietarios.toLocaleString()}
              </div>
              <div className="text-gray-600">Proprietários</div>
            </div>
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                {homeStats.totalContratos.toLocaleString()}
              </div>
              <div className="text-gray-600">Contratos Fechados</div>
            </div>
            <div className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-blue-600 mb-2">
                R$ {homeStats.mediaPreco.toLocaleString()}
              </div>
              <div className="text-gray-600">Preço Médio</div>
            </div>
          </div>
        </div>
      </section>

      {/* Tipos de Propriedade */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Encontre o tipo ideal
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Temos opções para todos os perfis e necessidades
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {propertyTypes.map((type) => (
              <Link
                key={type.tipo}
                href={`/imoveis?tipo=${type.tipo}`}
                className="bg-white rounded-xl p-6 shadow-sm hover:shadow-md transition-all duration-300 text-center group"
              >
                <div className="text-blue-600 mb-4 flex justify-center group-hover:scale-110 transition-transform">
                  {getPropertyTypeIcon(type.icone)}
                </div>
                <h3 className="text-xl font-semibold text-gray-900 mb-2">
                  {type.nome}
                </h3>
                <p className="text-gray-600 mb-3">
                  {type.descricao}
                </p>
                <div className="text-blue-600 font-medium">
                  {type.quantidade} disponíveis
                </div>
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Imóveis em Destaque */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between mb-12">
            <div>
              <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
                Imóveis em Destaque
              </h2>
              <p className="text-xl text-gray-600">
                Os melhores imóveis selecionados para você
              </p>
            </div>
            <Link
              href="/imoveis"
              className="hidden md:flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium"
            >
              Ver todos
              <ArrowRight className="h-5 w-5" />
            </Link>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {featuredProperties.map((imovel) => (
              <PropertyCard key={imovel.id} imovel={imovel} />
            ))}
          </div>

          <div className="text-center mt-8 md:hidden">
            <Link
              href="/imoveis"
              className="inline-flex items-center gap-2 bg-blue-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-blue-700 transition-colors"
            >
              Ver todos os imóveis
              <ArrowRight className="h-5 w-5" />
            </Link>
          </div>
        </div>
      </section>

      {/* Recursos e Benefícios */}
      <section className="py-16 bg-gray-50">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
              Por que escolher o ChaveCerta?
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Oferecemos a melhor experiência em aluguel de imóveis
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="text-center">
              <div className="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Shield className="h-8 w-8 text-blue-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                Segurança Garantida
              </h3>
              <p className="text-gray-600">
                Todos os imóveis e proprietários são verificados para sua segurança
              </p>
            </div>

            <div className="text-center">
              <div className="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Clock className="h-8 w-8 text-green-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                Processo Rápido
              </h3>
              <p className="text-gray-600">
                Encontre e alugue seu imóvel em poucos cliques, sem burocracia
              </p>
            </div>

            <div className="text-center">
              <div className="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                <Award className="h-8 w-8 text-purple-600" />
              </div>
              <h3 className="text-xl font-semibold text-gray-900 mb-2">
                Qualidade Premium
              </h3>
              <p className="text-gray-600">
                Imóveis de qualidade com fotos reais e informações detalhadas
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Call to Action */}
      <section className="py-16 bg-blue-600 text-white">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl md:text-4xl font-bold mb-4">
            Pronto para encontrar seu novo lar?
          </h2>
          <p className="text-xl mb-8 text-blue-100 max-w-2xl mx-auto">
            Junte-se a milhares de pessoas que já encontraram o imóvel dos sonhos
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/imoveis"
              className="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-gray-100 transition-colors"
            >
              Buscar Imóveis
            </Link>
            <Link
              href="/cadastro"
              className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white hover:text-blue-600 transition-colors"
            >
              Cadastrar Imóvel
            </Link>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-12">
        <div className="container mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center">
                  <span className="text-white font-bold">C</span>
                </div>
                <span className="text-xl font-bold">ChaveCerta</span>
              </div>
              <p className="text-gray-400 mb-4">
                A plataforma mais completa para aluguel de imóveis no Brasil.
              </p>
              <div className="flex items-center text-gray-400">
                <Star className="h-5 w-5 text-yellow-500 mr-1" />
                <span>4.8/5 de satisfação</span>
              </div>
            </div>

            <div>
              <h3 className="text-lg font-semibold mb-4">Para Inquilinos</h3>
              <ul className="space-y-2 text-gray-400">
                <li><Link href="/imoveis" className="hover:text-white transition-colors">Buscar Imóveis</Link></li>
                <li><Link href="/favoritos" className="hover:text-white transition-colors">Meus Favoritos</Link></li>
                <li><Link href="/contratos" className="hover:text-white transition-colors">Meus Contratos</Link></li>
              </ul>
            </div>

            <div>
              <h3 className="text-lg font-semibold mb-4">Para Proprietários</h3>
              <ul className="space-y-2 text-gray-400">
                <li><Link href="/cadastro-imovel" className="hover:text-white transition-colors">Cadastrar Imóvel</Link></li>
                <li><Link href="/dashboard" className="hover:text-white transition-colors">Meus Imóveis</Link></li>
                <li><Link href="/relatorios" className="hover:text-white transition-colors">Relatórios</Link></li>
              </ul>
            </div>

            <div>
              <h3 className="text-lg font-semibold mb-4">Suporte</h3>
              <ul className="space-y-2 text-gray-400">
                <li><Link href="/ajuda" className="hover:text-white transition-colors">Central de Ajuda</Link></li>
                <li><Link href="/contato" className="hover:text-white transition-colors">Contato</Link></li>
                <li><Link href="/termos" className="hover:text-white transition-colors">Termos de Uso</Link></li>
                <li><Link href="/privacidade" className="hover:text-white transition-colors">Privacidade</Link></li>
              </ul>
            </div>
          </div>

          <div className="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400">
            <p>&copy; 2024 ChaveCerta. Todos os direitos reservados.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
