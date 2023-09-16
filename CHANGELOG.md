# Changelog

## v1.7.3 (14/09/2023)
## Changes
## 🔧 Maintenance

- Create run_scanners for api and exclude unwanted outputs @JustinWonjaePark (#140)
- Add test for fl scanner and fl android @JustinWonjaePark (#139)

---

## v1.7.2 (31/08/2023)
## Changes
## 🐛 Hotfixes

- Fix vulnerability from requirements.txt @JustinWonjaePark (#138)

---

## v1.7.1 (31/08/2023)
## Changes
## 🔧 Maintenance

- Priority change between Download Location extraction and scanner operation @JustinWonjaePark (#133)

---

## v1.7.0 (14/08/2023)
## Changes
- Fix the bug when nothing is detected @soimkim (#134)

## 🚀 Features

- Load v32 and later of ScanCode @soimkim (#131)

## 🔧 Maintenance

- Fix the scancdoe and util version @dd-jy (#132)

---

## v1.6.32 (03/08/2023)
## Changes
## 🐛 Hotfixes

- Fix the util version @dd-jy (#130)

---

## v1.6.31 (03/08/2023)
## Changes
## 🐛 Hotfixes

- Revert the scancode-toolkit version @dd-jy (#129)

## 🔧 Maintenance

- Remove sorting @JustinWonjaePark (#128)

---

## v1.6.30 (25/07/2023)
## Changes
## 🔧 Maintenance

- Update scancode-toolkit version @dd-jy (#127)

---

## v1.6.29 (25/07/2023)
## Changes
## 🚀 Features

- Read download location @JustinWonjaePark (#124)

## 🐛 Hotfixes

- Update FOSSLight Util version @soimkim (#126)

## 🔧 Maintenance

- Sort the result by file and exclude attributes @JustinWonjaePark (#125)
- Update the minimum version of util @dd-jy (#123)
- Change the default path to find sbom-info.yaml @dd-jy (#122)

---

## v1.6.28 (02/06/2023)
## Changes
## 🔧 Maintenance

- Update the minimum version of util @dd-jy (#123)
- Change the default path to find sbom-info.yaml @dd-jy (#122)

---

## v1.6.27 (19/05/2023)
## Changes
## 🚀 Features

- Add to correct with sbom-info.yaml @dd-jy (#120)

## 🐛 Hotfixes

- Remove empty scanoss reference @JustinWonjaePark (#119)

## 🔧 Maintenance

- Fixed scancode-toolkit version @dd-jy (#118)

---

## v1.6.26 (17/04/2023)
## Changes
## 🐛 Hotfixes

- Update the ubuntu version for deploy action @dd-jy (#117)
- Remove SPDX, URL from copyright @soimkim (#115)

## 🔧 Maintenance

- Fix Scancode error in Python 3.7 @soimkim (#116)

---

## v1.6.25 (27/02/2023)
## Changes
## 🔧 Maintenance

- Update git user in release action @bjk7119 (#114, #113)
- Add the package name to result in the missing file @dd-jy (#112)
- Add the package name to log and result file @dd-jy (#111)
- Add the core option in help message @dd-jy (#110)
- Unify version output format @bjk7119 (#109)
- Change package to get release package @bjk7119 (#108)
- Update version of packages for actions @bjk7119 (#107)

---

## v1.6.24 (02/01/2023)
## Changes
## 🐛 Hotfixes

- Fix omitted Scanoss result at -m option @JustinWonjaePark (#106)
- Remove warning for -m option with default output @JustinWonjaePark (#104)

## 🔧 Maintenance

- Remove warranty-disclaimer from license detected by ScanCode @JustinWonjaePark (#105)
- Revert "Fix ScanCode's import LegacyVersion bug" @soimkim (#103)

---

## v1.6.23 (23/12/2022)
## Changes
## 🔧 Maintenance

- Revert "Clear ScanCode cache after installation" @soimkim (#102)

---

## v1.6.22 (23/12/2022)
## Changes
## 🐛 Hotfixes

- Clear ScanCode cache after installation @soimkim (#101)

---

## v1.6.21 (08/12/2022)
## Changes
## 🔧 Maintenance

- Add parameter for Scancode cores @soimkim (#100)

---

## v1.6.20 (18/11/2022)
## Changes
## 🐛 Hotfixes

- Block -m option for opossum,yaml and csv @JustinWonjaePark (#98)

---

## v1.6.19 (04/11/2022)
## Changes
- Unify help message for source scanner and converter @JustinWonjaePark (#97)

## 🐛 Hotfixes

- Remove the last dot from the result in scanoss license finding @JustinWonjaePark (#95)

## 🔧 Maintenance

- Change argument parsing for convert to argpars @JustinWonjaePark (#94, #96)

---

## v1.6.18 (15/09/2022)
## Changes
## 🔧 Maintenance

- Change the output file name @JustinWonjaePark (#93)

---

## v1.6.17 (13/09/2022)
## Changes
## 🐛 Hotfixes

- Fix the bug that can't extract copyright @soimkim (#92)

---

## v1.6.16 (01/09/2022)
## Changes
## 🐛 Hotfixes

- Fix a bug when reading a non-existent key @soimkim (#89)

## 🔧 Maintenance

- Do not print empty parsing messages @soimkim (#91)
- Change the required version of Python to 3.7 @soimkim (#90)

---

## v1.6.15 (12/08/2022)
## Changes
- Remove the required option from the help message @soimkim (#87)

---

## v1.6.14 (04/08/2022)
## Changes
## 🐛 Hotfixes

- Fix the bug that convert mode does not run @soimkim (#84)
- Fix package download bug during docker build @soimkim (#80)

## 🔧 Maintenance

- Print tool information to log @soimkim (#86)
- Analyze the current path if path is null @soimkim (#85)
- Print the message if there is nothing to print @soimkim (#83)

---

## v1.6.13 (27/06/2022)
## Changes
## 🚀 Features

- Add option for time out @soimkim (#79)

---

## v1.6.12 (17/06/2022)
## Changes
## 🐛 Hotfixes

- Fix typecode-libmagic-from-sources installation bug @soimkim (#77)

---

## v1.6.11 (16/06/2022)
## Changes
## 🚀 Features

- Add yaml format for FOSSLight Report @dd-jy (#75)

## 🔧 Maintenance

- update minimum version of fosslight_util @dd-jy (#76)

---

## v1.6.10 (02/06/2022)
## Changes
- Amend how to handle path without files to scan for SCANOSS @JustinWonjaePark (#73)
- Refine license name on SCANOSS results @JustinWonjaePark (#74)

## 🚀 Features

- Print SCANOSS info in a separate sheet @JustinWonjaePark (#72)
- Add Dockerfile to build on ubuntu @soimkim (#69)

## 🐛 Hotfixes

- Fix cli.py to remove redundant report @JustinWonjaePark (#71)

---

## v1.6.9 (06/04/2022)
## Changes
## 🐛 Hotfixes

- Fix errors that occur in Python 3.6.7 or lower @soimkim (#67)

## 🔧 Maintenance

- Add a commit message checker @soimkim (#66)
---

## v1.6.8 (11/03/2022)
## Changes
## 🔧 Maintenance

- Change the scanoss-related packages @soimkim (#63)

---

## v1.6.7 (10/02/2022)
## Changes
## 🚀 Features

- Add license reference column @JustinWonjaePark (#59)

## 🔧 Maintenance

- Amend to print output file name and deal with format option error @JustinWonjaePark (#62)
