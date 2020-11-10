#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fdm_materials
Version  : 4.8
Release  : 12
URL      : https://github.com/Ultimaker/fdm_materials/archive/4.8/fdm_materials-4.8.tar.gz
Source0  : https://github.com/Ultimaker/fdm_materials/archive/4.8/fdm_materials-4.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0
Requires: fdm_materials-data = %{version}-%{release}
Requires: fdm_materials-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : git

%description
No detailed description available

%package data
Summary: data components for the fdm_materials package.
Group: Data

%description data
data components for the fdm_materials package.


%package license
Summary: license components for the fdm_materials package.
Group: Default

%description license
license components for the fdm_materials package.


%prep
%setup -q -n fdm_materials-4.8
cd %{_builddir}/fdm_materials-4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605032522
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1605032522
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fdm_materials
cp %{_builddir}/fdm_materials-4.8/LICENSE %{buildroot}/usr/share/package-licenses/fdm_materials/5f66eb3703482d8c327484f5b29041e8104d1e38
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cura/resources/materials/Vertex_Delta_ABS.xml.fdm_material
/usr/share/cura/resources/materials/Vertex_Delta_PET.xml.fdm_material
/usr/share/cura/resources/materials/Vertex_Delta_PLA.xml.fdm_material
/usr/share/cura/resources/materials/Vertex_Delta_PLA_Glitter.xml.fdm_material
/usr/share/cura/resources/materials/Vertex_Delta_PLA_Mat.xml.fdm_material
/usr/share/cura/resources/materials/Vertex_Delta_PLA_Satin.xml.fdm_material
/usr/share/cura/resources/materials/Vertex_Delta_PLA_Wood.xml.fdm_material
/usr/share/cura/resources/materials/Vertex_Delta_TPU.xml.fdm_material
/usr/share/cura/resources/materials/chromatik_pla.xml.fdm_material
/usr/share/cura/resources/materials/dsm_arnitel2045_175.xml.fdm_material
/usr/share/cura/resources/materials/dsm_novamid1070_175.xml.fdm_material
/usr/share/cura/resources/materials/eSUN_PETG_Black.xml.fdm_material
/usr/share/cura/resources/materials/eSUN_PETG_Grey.xml.fdm_material
/usr/share/cura/resources/materials/eSUN_PETG_Purple.xml.fdm_material
/usr/share/cura/resources/materials/eSUN_PLA_PRO_Black.xml.fdm_material
/usr/share/cura/resources/materials/eSUN_PLA_PRO_Grey.xml.fdm_material
/usr/share/cura/resources/materials/eSUN_PLA_PRO_Purple.xml.fdm_material
/usr/share/cura/resources/materials/eSUN_PLA_PRO_White.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_abs.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_absx.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_acetate.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_asax.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_bvoh.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_hips.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_petg.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_pla.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_pva-m.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_pva-s.xml.fdm_material
/usr/share/cura/resources/materials/emotiontech_tpu98a.xml.fdm_material
/usr/share/cura/resources/materials/fabtotum_abs.xml.fdm_material
/usr/share/cura/resources/materials/fabtotum_nylon.xml.fdm_material
/usr/share/cura/resources/materials/fabtotum_pla.xml.fdm_material
/usr/share/cura/resources/materials/fabtotum_tpu.xml.fdm_material
/usr/share/cura/resources/materials/fiberlogy_hd_pla.xml.fdm_material
/usr/share/cura/resources/materials/filo3d_pla.xml.fdm_material
/usr/share/cura/resources/materials/filo3d_pla_green.xml.fdm_material
/usr/share/cura/resources/materials/filo3d_pla_red.xml.fdm_material
/usr/share/cura/resources/materials/generic_abs.xml.fdm_material
/usr/share/cura/resources/materials/generic_abs_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_bam.xml.fdm_material
/usr/share/cura/resources/materials/generic_cffcpe.xml.fdm_material
/usr/share/cura/resources/materials/generic_cffpa.xml.fdm_material
/usr/share/cura/resources/materials/generic_cpe.xml.fdm_material
/usr/share/cura/resources/materials/generic_cpe_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_cpe_plus.xml.fdm_material
/usr/share/cura/resources/materials/generic_gffcpe.xml.fdm_material
/usr/share/cura/resources/materials/generic_gffpa.xml.fdm_material
/usr/share/cura/resources/materials/generic_hips.xml.fdm_material
/usr/share/cura/resources/materials/generic_hips_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_nylon.xml.fdm_material
/usr/share/cura/resources/materials/generic_nylon_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_pc.xml.fdm_material
/usr/share/cura/resources/materials/generic_pc_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_petg.xml.fdm_material
/usr/share/cura/resources/materials/generic_petg_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_pla.xml.fdm_material
/usr/share/cura/resources/materials/generic_pla_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_pp.xml.fdm_material
/usr/share/cura/resources/materials/generic_pva.xml.fdm_material
/usr/share/cura/resources/materials/generic_pva_175.xml.fdm_material
/usr/share/cura/resources/materials/generic_tough_pla.xml.fdm_material
/usr/share/cura/resources/materials/generic_tpu.xml.fdm_material
/usr/share/cura/resources/materials/generic_tpu_175.xml.fdm_material
/usr/share/cura/resources/materials/imade3d_petg_175.xml.fdm_material
/usr/share/cura/resources/materials/imade3d_pla_175.xml.fdm_material
/usr/share/cura/resources/materials/innofill_innoflex60_175.xml.fdm_material
/usr/share/cura/resources/materials/leapfrog_abs_natural.xml.fdm_material
/usr/share/cura/resources/materials/leapfrog_epla_natural.xml.fdm_material
/usr/share/cura/resources/materials/leapfrog_pva_natural.xml.fdm_material
/usr/share/cura/resources/materials/octofiber_pla.xml.fdm_material
/usr/share/cura/resources/materials/polyflex_pla.xml.fdm_material
/usr/share/cura/resources/materials/polymax_pla.xml.fdm_material
/usr/share/cura/resources/materials/polyplus_pla.xml.fdm_material
/usr/share/cura/resources/materials/polywood_pla.xml.fdm_material
/usr/share/cura/resources/materials/redd_abs.xml.fdm_material
/usr/share/cura/resources/materials/redd_asa.xml.fdm_material
/usr/share/cura/resources/materials/redd_hips.xml.fdm_material
/usr/share/cura/resources/materials/redd_nylon.xml.fdm_material
/usr/share/cura/resources/materials/redd_petg.xml.fdm_material
/usr/share/cura/resources/materials/redd_pla.xml.fdm_material
/usr/share/cura/resources/materials/redd_tpe.xml.fdm_material
/usr/share/cura/resources/materials/structur3d_dap100silicone.xml.fdm_material
/usr/share/cura/resources/materials/tizyx_abs.xml.fdm_material
/usr/share/cura/resources/materials/tizyx_flex.xml.fdm_material
/usr/share/cura/resources/materials/tizyx_petg.xml.fdm_material
/usr/share/cura/resources/materials/tizyx_pla.xml.fdm_material
/usr/share/cura/resources/materials/tizyx_pla_bois.xml.fdm_material
/usr/share/cura/resources/materials/tizyx_pva.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_blue.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_green.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_grey.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_orange.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_pearl-gold.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_red.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_silver-metallic.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_white.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_abs_yellow.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_bam.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_blue.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_dark-grey.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_green.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_light-grey.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_plus_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_plus_transparent.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_plus_white.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_red.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_transparent.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_white.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_cpe_yellow.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_nylon_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_nylon_transparent.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pc_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pc_transparent.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pc_white.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_blue.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_green.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_magenta.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_orange.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_pearl-white.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_red.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_silver-metallic.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_transparent.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_white.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pla_yellow.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pp_transparent.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_pva.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tough_pla_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tough_pla_green.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tough_pla_red.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tough_pla_white.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tpu_black.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tpu_blue.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tpu_red.xml.fdm_material
/usr/share/cura/resources/materials/ultimaker_tpu_white.xml.fdm_material
/usr/share/cura/resources/materials/verbatim_bvoh_175.xml.fdm_material
/usr/share/cura/resources/materials/zyyx_pro_flex.xml.fdm_material
/usr/share/cura/resources/materials/zyyx_pro_pla.xml.fdm_material

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fdm_materials/5f66eb3703482d8c327484f5b29041e8104d1e38
