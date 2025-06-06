/**
 * Tipos TypeScript para o sistema ChaveCerta
 * 
 * Este arquivo contém todas as interfaces e tipos utilizados
 * na aplicação frontend do ChaveCerta.
 */

// ============================================================================
// TIPOS BÁSICOS
// ============================================================================

/**
 * Interface base para entidades que possuem ID
 */
export interface BaseEntity {
  id: number;
  created_at: string;
  updated_at: string;
}

/**
 * Interface para dados de usuário
 */
export interface User extends BaseEntity {
  email: string;
  nome: string;
  telefone?: string;
  imagem_perfil?: string;
  tipo_usuario: 'proprietario' | 'inquilino';
  is_active: boolean;
}

/**
 * Interface para dados de imóvel
 */
export interface Imovel extends BaseEntity {
  titulo: string;
  descricao: string;
  tipo: 'casa' | 'apartamento' | 'kitnet' | 'comercial';
  endereco: string;
  cidade: string;
  estado: string;
  cep: string;
  preco_mensal: number;
  area_m2: number;
  quartos: number;
  banheiros: number;
  vagas_garagem: number;
  mobiliado: boolean;
  permite_pets: boolean;
  disponivel: boolean;
  proprietario: User;
  imagens: string[];
  amenidades: string[];
  latitude?: number;
  longitude?: number;
}

// ============================================================================
// TIPOS PARA COMPONENTES
// ============================================================================

/**
 * Props para cards de imóveis
 */
export interface PropertyCardProps {
  imovel: Imovel;
  variant?: 'grid' | 'list';
  showFavorite?: boolean;
  onFavoriteClick?: (imovelId: number) => void;
}

/**
 * Props para componentes de busca
 */
export interface SearchFormData {
  cidade: string;
  tipo?: string;
  precoMin?: number;
  precoMax?: number;
  quartos?: number;
}

/**
 * Props para seções da home page
 */
export interface HeroSectionProps {
  onSearch: (data: SearchFormData) => void;
}

export interface FeaturedPropertiesProps {
  imoveis: Imovel[];
  loading?: boolean;
}

// ============================================================================
// TIPOS PARA ESTATÍSTICAS DA HOME
// ============================================================================

/**
 * Interface para estatísticas exibidas na home
 */
export interface HomeStats {
  totalImoveis: number;
  totalProprietarios: number;
  totalContratos: number;
  mediaPreco: number;
}

/**
 * Interface para tipos de propriedade em destaque
 */
export interface PropertyType {
  tipo: string;
  nome: string;
  descricao: string;
  icone: string;
  quantidade: number;
}
